from django.db import models
from accounts.models import Teacher
# Create your models here.

#Course information
class Course(models.Model):
    user_id = models.ForeignKey(Teacher, verbose_name="Teacher ID")
    course_id = models.IntegerField(primary_key=True, verbose_name="Course ID")
    name = models.TextField(verbose_name="Course Name")

#Student information
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True, verbose_name="Student ID")
    name = models.CharField(max_length=150, verbose_name="Student Name")
    whatsapp = models.BooleanField(verbose_name="Whatsapp Availability")
    mobile = models.BigIntegerField(null=True,blank=True,verbose_name="Mobile Number")


class StudentMarks(models.Model):
    student_id = models.ForeignKey(Student, verbose_name="Student ID")
    course_id = models.ForeignKey(Course,verbose_name="Course ID")
    name = models.TextField(verbose_name="Course Name")
    marks = models.IntegerField(verbose_name="Quiz Marks")

#Quiz Sent
class QuizSent(models.Model):
    quiz_id = models.IntegerField(primary_key=True, verbose_name="Quiz Sent ID")
    mobile_number = models.ForeignKey(Student,verbose_name="Mobile Number")
    description = models.TextField(verbose_name="Quiz Description")
    total_marks = models.IntegerField(verbose_name="Total Marks")

#Quiz Received
class QuizReceived(models.Model):
    quiz_id = models.ForeignKey(QuizSent, primary_key=True, verbose_name="Quiz Sent ID")
    student_id = models.ForeignKey(Student , verbose_name="Student ID")
    marks = models.IntegerField(verbose_name="Quiz Marks")
