from twilio.rest import Client
import os
import sqlite3
import shutil
import getpass
import pathlib
from twilio.rest import Client
from twilio import twiml


def get_no():
    extrct = sqlite3.connect('db.sqlite3')
    db = history_con.cursor()
    db.execute("SELECT mobile FROM courses_Student WHERE ")
    results = db.fetchall()
    for r in range(len(results)):
        results[r] = list(results[r])
    extrct.close()
    return results


def send_sms(message):
    # Your Account Sid and Auth Token from twilio.com / console
    account_sid = 'AC47d3b372588f0f8b935c43f7b18ca306'
    auth_token = 'ffd2cbddbe938fcbcc64843f7fe60862'


    client = Client(account_sid, auth_token)

    #test
    message = client.messages.create(
        from_='+16039414130',
        body='body',
        to='+919714948808'
    )

    mobile_no = get_no()
    print(mobile_no)

    for x in mobile_no:
        message = client.messages.create(
            from_='+16039414130',
            body=message,
            to=str(x)
        )
        print(message.sid)


send_sms()
