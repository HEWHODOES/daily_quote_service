
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

print("starting script")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAIL,
    subject="This is a TEST",
    html_content='<strong>Hello!<strong><p>Seems like it worked!!'
)
print("trying to send email")
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(f"Email sent! Status: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")    