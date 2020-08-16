# Django SECRET_KEY for sessions
SECRET_KEY = 'development key'  # change this to a secret string when deploying

# Twilio credentials and phone number
# obtained from twilio.com/console
TWILIO_ACCOUNT_SID = 'AC47d3b372588f0f8b935c43f7b18ca306 '
# also obtained from twilio.com/console
TWILIO_AUTH_TOKEN = 'ffd2cbddbe938fcbcc64843f7fe60862 '
TWILIO_NUMBER = '+919714948808'  # use the number you received when signing up or buy a new number
SMS_BROADCAST_TO_NUMBERS= [
     '+919714948808',
 ]
