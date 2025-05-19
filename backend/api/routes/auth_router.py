"""
auth_router.py 🔐
---------------------
Robust FastAPI authentication system:
- Secure password hashing (argon2)
- Email verification & reset (OTP codes)
- Optional pin & 2FA fields
- All data stored encrypted in SQL backend

See your MemoryRouter + EncryptedMemoryEngine for storage!
"""

import os, time, jwt, secrets, smtplib
from fastapi import APIRouter, HTTPException, status, Request
from pydantic import BaseModel, EmailStr, field_validator
from argon2 import PasswordHasher
from email_validator import validate_email, EmailNotValidError
from shared.memory.memory_router import MemoryRouter
from backend.utils.email_utils import send_verification_email, send_reset_email
from typing import Annotated

JWT_SECRET = os.environ.get("JWT_SECRET", secrets.token_urlsafe(32))
JWT_EXPIRE_S = 60 * 60 * 6  # 6 hours, tunable

router = APIRouter(prefix="/api/auth", tags=["Auth"])
store = MemoryRouter(mode="sql", encrypt=True)
ph = PasswordHasher()

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
FROM_EMAIL = GMAIL_ADDRESS

class RegisterReq(BaseModel):
    email: EmailStr
    password: Annotated[str, {"min_length": 8}]
    pin: Annotated[str | None, {"min_length": 4, "max_length": 8}] = None

    # Optional: Add custom strict checkers if you want!
    @field_validator("password")
    def password_strength(cls, v):
        if " " in v:
            raise ValueError("Password must not contain spaces")
        return v

class UserRecord(BaseModel):
    email: EmailStr
    password: Annotated[str, {"min_length": 8}]
    pin: Annotated[str | None, {"min_length": 4, "max_length": 8}] = None
    os_user: str = None
    verified: bool = False
    reset_otp: str = None
    reset_otp_expiry: float = 0
    last_login: float = 0.0

# Helper: fetch user dict (or None)
def _get(email):
    return store.fetch("user", email.lower()) or None

def _save(email, data):
    store.save("user", email.lower(), data)

# Helper: generate JWT for user
def _gen_jwt(email):
    payload = {"email": email, "exp": int(time.time()) + JWT_EXPIRE_S}
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

# Registration
class RegisterReq(BaseModel):
    email: EmailStr
    password: Annotated[str, {"min_length": 8}]
    pin: Annotated[str | None, {"min_length": 4, "max_length": 8}] = None

@router.post("/register")
def register_user(req: RegisterReq):
    try:
        validate_email(req.email)
    except EmailNotValidError as e:
        raise HTTPException(400, str(e))
    if _get(req.email):
        raise HTTPException(400, "Email already registered.")

    rec = UserRecord(
        email=req.email,
        password=ph.hash(req.password),
        pin=req.pin,
        verified=False,
    )
    _save(req.email, rec.dict())
    code = secrets.token_urlsafe(6)
    rec.reset_otp = code
    rec.reset_otp_expiry = time.time() + 600
    _save(req.email, rec.dict())
    # Send via Gmail SMTP
    send_email(req.email, "Your HivemindOS Verification Code", f"Your code: {code}\n(Expires in 10 mins)")
    print(f"[DEV] Verification code sent to {req.email}: {code}")
    return {"ok": True, "msg": "Verification sent."}

# Email verification (for demo: combined with reset)
@router.post("/verify")
def verify_email(email: EmailStr, code: str):
    rec = _get(email)
    if not rec or not rec.get("reset_otp") or time.time() > rec.get("reset_otp_expiry", 0):
        raise HTTPException(400, "No pending verification or code expired.")
    if secrets.compare_digest(rec["reset_otp"], code):
        rec["verified"] = True
        rec["reset_otp"] = None
        rec["reset_otp_expiry"] = 0
        _save(email, rec)
        return {"ok": True}
    raise HTTPException(400, "Invalid code.")

# Login!
class LoginReq(BaseModel):
    email: EmailStr
    password: str
    code: str = None  # for 2FA

@router.post("/login")
def login_user(req: LoginReq, request: Request):
    rec = _get(req.email)
    os_user = dict(request.headers).get("x-os-user") or os.getenv("USER", "guest")
    if not rec:
        raise HTTPException(401, "Incorrect credentials.")
    if not rec.get("verified"):
        raise HTTPException(401, "Account not verified.")
    try:
        ph.verify(rec["password"], req.password)
    except Exception:
        raise HTTPException(401, "Incorrect credentials.")
    # 2FA
    if rec.get("pin") and (not req.code or rec["pin"] != req.code):
        raise HTTPException(401, "Pin/2FA required.")
    rec["last_login"] = time.time()
    rec["os_user"] = os_user
    _save(req.email, rec)
    token = _gen_jwt(req.email)
    return {"token": token, "ok": True}

# Forgot password request
@router.post("/request_reset")
def request_reset(email: EmailStr):
    rec = _get(email)
    if not rec:
        return {"ok": True}
    code = secrets.token_urlsafe(6)
    rec["reset_otp"] = code
    rec["reset_otp_expiry"] = time.time() + 600
    _save(email, rec)
    send_email(email, "Reset Your Password", f"Code: {code}\n(Expires in 10 mins)")
    return {"ok": True}

class ResetReq(BaseModel):
    email: EmailStr
    code: str
    new_password: Annotated[str, {"min_length": 8}]


# Complete password reset
@router.post("/reset_password")
def reset_password(req: ResetReq):
    rec = _get(req.email)
    if not rec or rec.get("reset_otp") != req.code or time.time() > rec.get("reset_otp_expiry", 0):
        raise HTTPException(400, "Invalid or expired code.")
    rec["password"] = ph.hash(req.new_password)
    rec["reset_otp"] = None
    rec["reset_otp_expiry"] = 0
    _save(req.email, rec)
    return {"ok": True}

# For "remember me": auto-login via OS user if matched
@router.get("/auto_login")
def auto_login(request: Request):
    os_user = dict(request.headers).get("x-os-user") or os.getenv("USER", "guest")
    # Scan all users for a match (inefficient for demo; optimize with index for prod)
    for email in ("user",):  # 'user' is the prefix for email-key for demo, replace with list.
        rec = store.fetch("user", email)
        if rec and rec.get("os_user") == os_user:
            token = _gen_jwt(email)
            return {"ok": True, "email": email, "token": token}
    return {"ok": False}

# Utility to get current user from JWT (add as dependency in protected routes as needed!)
def get_current_email(request: Request):
    auth = request.headers.get("authorization", "")
    try:
        token = auth.replace("Bearer ", "")
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        email = payload.get("email")
        return email
    except Exception:
        raise HTTPException(401, "Missing or invalid token.")
    
def send_email(recipient: str, subject: str, body: str):
    """
    Simple Gmail SMTP sender using app password.

    Args:
        recipient (str): Who to send to
        subject (str): Subject line
        body (str): Message body (plaintext)
    """
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            msg = f"From: {FROM_EMAIL}\r\nTo: {recipient}\r\nSubject: {subject}\r\n\r\n{body}"
            smtp.sendmail(FROM_EMAIL, recipient, msg)
    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send email to {recipient}: {e}")
