from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

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


    def make_call(self, to_phone, message):
        """
        Makes a voice call using Twilio
        :param to_phone: Destination phone number
        :param message: Message to be spoken in the call
        """
        # Create TwiML response
        response = VoiceResponse()
        response.say(message)
        response.pause(length=1)
        response.say(message)  # Repeat the message

        # Make the call with inline TwiML
        self.twilio_client.calls.create(
            twiml=str(response),
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
