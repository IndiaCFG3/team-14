from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Teacher(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    
=======
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    phoneno=models.BigIntegerField(null=True,blank=True, verbose_name="Mobile Number")
>>>>>>> 0c6f900de8cee328f7a8e2e79786e35bfdc80113
