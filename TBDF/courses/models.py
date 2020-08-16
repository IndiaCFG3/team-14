from django.db import models
from account.models import Teacher
# Create your models here.

#Course information
class Course(models.Model):
    teacher_id = models.ForeignKey(Teacher, verbose_name="Teacher ID")
    course_id = models.IntegerField(verbose_name="Course ID")
    name = models.TextField(verbose_name="Course Name")


#Message Sending
class MessageSender(models.Model):
    msg_id = models.IntegerField(verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Sent Time")
    course_id = models.ForeignKey(Course,verbose_name="Course ID")
    description = models.TextField(verbose_name="Description")

#Message Receiving
class MessageReceiver(models.Model):
    msg_id = models.IntegerField(verbose_name="Message ID")
    timestamp = models.DateTimeField(auto_now=True, verbose_name="Received Time")
    mobile_number = models.ForeignKey(,verbose_name="Mobile Number")
    description = models.TextField(verbose_name="Description")

#Quiz Sent
class QuizSent(models.Model):
    quiz_id = models.IntegerField(verbose_name="Quiz Sent ID")
    mobile_number = models.ForeignKey(,verbose_name="Mobile Number")
    description = models.TextField(verbose_name="Quiz Description")
    total_marks = models.IntegerField(verbose_name="Total Marks")

#Quiz Received
class QuizReceived(models.Model):
    quiz_id = models.ForeignKey(QuizSent, verbose_name="Quiz Sent ID")
    student_id = models.ForeignKey( , verbose_name="Student ID")
    marks = models.IntegerField(verbose_name="Quiz Marks")
