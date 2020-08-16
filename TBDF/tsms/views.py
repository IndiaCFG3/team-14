from . import secretkey
from django.http import HttpResponse
from twilio.rest import Client


def tsms_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                            "yet? Grab it here: https://www.twilio.com/quest")
    client = Client(secretkey.TWILIO_ACCOUNT_SID, secretkey.TWILIO_AUTH_TOKEN)
    for recipient in secretkey.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=secretkey.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
