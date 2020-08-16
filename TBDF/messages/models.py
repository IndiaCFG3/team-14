from django.db import models

# Create your models here.
#Message Sending
class MessageSender(models.Model):
    msg_id = models.IntegerField(primary_key=True, verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Sent Time")
    course_id = models.ForeignKey(Course,verbose_name="Course ID")
    description = models.TextField(verbose_name="Description")

#Message Receiving
class MessageReceiver(models.Model):
    msg_id = models.IntegerField(primary_key=True, verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Received Time")
    mobile_number = models.ForeignKey(Student,verbose_name="Mobile Number")
    description = models.TextField(verbose_name="Description")
