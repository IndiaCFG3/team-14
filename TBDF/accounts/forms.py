from django import forms
from accounts.models import Teacher



class TeacherRegisterForm(form.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'username',
                  'password1', 'password2', 'age', 'gender', 'phoneno', 'address']
    
