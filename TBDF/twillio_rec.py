from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from twilio.rest import Client
import os
import sqlite3
from twilio.rest import Client
from flask import Flask, request
from twilio import twiml
import os 


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Message received")
    
    writecn = sqlite3.connect('db.sqlite3')
    db = history_con.cursor()
    db.execute("INSERT INTO tsms_messagereceiver (description,mobile_number) Values(" +str(resp.message)+str(resp.mobile_no) +")")
    print("Message received")
    writecn.close()
    
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)


