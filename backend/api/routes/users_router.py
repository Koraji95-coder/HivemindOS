"""
users_router.py 🧑‍💼
----------------------
Admin-only endpoints for listing/managing users.
Integrates with MemoryRouter encrypted SQL backend.

Notes:
- Only "Dustin" (or admin match) can view all users.
- Does not expose private info (hashed passwords, pins).
- You must update 'admin_email' to your address!
"""

from fastapi import APIRouter, Request, Depends, HTTPException
from shared.memory.memory_router import MemoryRouter
from .auth_router import get_current_email
from typing import Annotated
import base64

router = APIRouter(prefix="/api/users", tags=["Users"])
store = MemoryRouter(mode="sql", encrypt=True)

# Change this to your email (must match registered user's)
ADMIN_EMAIL = "dustin@yourdomain.com"

def require_admin(request: Request):
    """
    Dependency to ensure only the admin sees user info.
    """
    email = get_current_email(request)
    if email.lower() != ADMIN_EMAIL:
        raise HTTPException(403, "Forbidden: Admins only.")
    return email

@router.get("/all")
def list_users(request: Request = Depends(require_admin)):
    """
    List all users, except passwords/pins.
    Scans all user keys in memory backend.

    Returns:
        List of dicts: {email, verified, last_login}
    """
    seen = []
    # Note: In production, you'd scan a table.
    # Here, scan known keys, e.g. "user:{email}" or whatever your MemoryEngine stores.
    engine = store.engine
    # This code assumes user keys are of the format: key="user", user=email
    # If using SQLAlchemy, query all MemoryRecords where user=='user'
    if hasattr(engine, "engine"):  # If it's SQLMemoryEngine
        # For illustration, let's say you query MemoryRecord model
        from shared.memory.sql_memory_engine import MemoryRecord, SessionLocal
        with SessionLocal() as db:
            records = db.query(MemoryRecord).filter(MemoryRecord.user == "user").all()
            for rec in records:
                try:
                    userdata = base64.b64decode(rec.value).decode()
                except Exception:
                    userdata = rec.value
                # Add email, verified, and last_login safely
                try:
                    import json
                    d = json.loads(userdata)
                    seen.append({
                        "email": d.get("email"),
                        "verified": d.get("verified"),
                        "last_login": d.get("last_login")
                    })
                except Exception:
                    continue
    else:
        # Non-SQL/legacy, just return empty
        pass
    return seen