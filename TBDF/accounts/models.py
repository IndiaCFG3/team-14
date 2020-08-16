from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age=models.IntegerField(null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    Education=models.CharField(max_length=500)
    Subject=models.CharField(max_length=500)
    
