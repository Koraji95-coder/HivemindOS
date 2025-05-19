"""
email_utils.py 📧
------------------
Email-sending utilities for auth (verification, reset, alerts).
Uses SendGrid API, but can easily be adapted for other providers.

# Usage:
from backend.utils.email_utils import send_verification_email, send_reset_email
send_verification_email("user@email.com", "OTP123")

For dev/test, you can swap out with a print statement or add SMS/other transports.
"""

import os
import sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
FROM_EMAIL = os.environ.get("FROM_EMAIL", "no-reply@your-app.com")

def send_verification_email(recipient: str, code: str) -> None:
    """
    Send an account verification code to the given email address.

    Args:
        recipient (str): Email address to send to
        code (str): The verification code to include
    """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    msg = Mail(
        from_email=FROM_EMAIL,
        to_emails=recipient,
        subject="Your HivemindOS Verification Code",
        plain_text_content=f"Your verification code: {code}\n\n(Expires in 10 minutes)",
    )
    try:
        sg.send(msg)
    except Exception as e:
        print(f"[ERROR] Failed to send verification email to {recipient}: {e}")

def send_reset_email(recipient: str, code: str) -> None:
    """
    Send a password reset code.

    Args:
        recipient (str): Email address
        code (str): Reset code
    """
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    msg = Mail(
        from_email=FROM_EMAIL,
        to_emails=recipient,
        subject="Reset Your HivemindOS Password",
        plain_text_content=f"Reset your password using this code: {code}\n\n(Expires in 10 minutes)",
    )
    try:
        sg.send(msg)
    except Exception as e:
        print(f"[ERROR] Failed to send reset email to {recipient}: {e}")

# -- READY FOR EXTENSION: SMS/alerts --
def send_sms(recipient_phone: str, message: str) -> None:
    """
    [Placeholder] Send SMS message (integrate with Twilio/Nexmo for prod).
    """
    print(f"[SMS to {recipient_phone}]: {message}")
    # TODO: Implement with actual SMS gateway (Twilio, etc.) if you wish!