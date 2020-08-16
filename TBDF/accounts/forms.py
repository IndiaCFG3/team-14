from django import forms
from accounts.models import Teacher


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True,),
    last_name = forms.CharField(max_length=100, required=True),
    email = forms.EmailField(required=True),

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email', 'username',
                  'password1', 'password2', ]



class TeacherRegisterForm(form.ModelForm):
    class Meta:
        model = Teacher
        fields = [ 'phoneno','Education','Subject']
    
