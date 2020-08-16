from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    phoneno=models.BigIntegerField(null=True,blank=True, verbose_name="Mobile Number")
