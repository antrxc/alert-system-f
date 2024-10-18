from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, EMAIL_PASSWORD, EMAIL_ADDRESS
import smtplib
from email.mime.text import MIMEText

class AlertService:
    def __init__(self):
        self.twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, to_phone, message):
        self.twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )

    def send_email(self, to_email, subject, message):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        from_email = EMAIL_ADDRESS
        password = EMAIL_PASSWORD

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
