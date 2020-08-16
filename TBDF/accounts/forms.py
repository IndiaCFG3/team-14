from django import forms
from accounts.models import Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True,),
    last_name = forms.CharField(max_length=100, required=True),
    email = forms.EmailField(required=True),

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username',
                  'password1', 'password2', ]


class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['phoneno']


class SendSmsForm(forms.ModelForm):
    class Meta:
        fields = ['description']
