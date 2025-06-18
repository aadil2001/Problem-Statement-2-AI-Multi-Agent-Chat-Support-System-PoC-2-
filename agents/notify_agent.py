from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

def notify_user(user_id: str, intent: str):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject="Support Notification",
        html_content=f"""
            <p>Hello <strong>{user_id}</strong>,</p>
            <p>Your request about <strong>{intent}</strong> has been received. We'll contact you shortly.</p>
        """
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("✅ Email sent. Status code:", response.status_code)
    except Exception as e:
        print("❌ SendGrid error:", e)
