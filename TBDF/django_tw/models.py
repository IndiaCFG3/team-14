from django.db import models
from twilio.rest import Client
from .auth import *


# Create your models here.
class message(models.Model):
    result = models.PositiveIntegerField()
    def __str__(self):
        return str(self.result)

    def save(self,*args,**kwargs):
        if self.result < 70:
            account_sid = sid
            auth_token = token
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hi there! - {self.result}',
                                        from_='+16039414130',
                                        to='+919714948808'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)