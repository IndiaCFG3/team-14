from django.db import models
from twilio.rest import Client
from courses.models import Course,Student
from .auth import *
# Create your models here.

class message(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
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

#Message Sending
class MessageSender(models.Model):
    msg_id = models.IntegerField(primary_key=True, verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Sent Time")
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Course ID")
    description = models.TextField(verbose_name="Description")

#Message Receiving
class MessageReceiver(models.Model):
    msg_id = models.IntegerField(primary_key=True, verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Received Time")
    mobile_number = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name="Mobile Number")
    description = models.TextField(verbose_name="Description")
