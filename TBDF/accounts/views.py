from django.shortcuts import render,messages
from django.http import request

# Create your views here.


from accounts.forms import UserRegisterForm,TeacherRegisterForm


def TeacherSignup(request):

    if request.method == 'POST':
        userform = UserRegisterForm(
            request.POST, request.FILES)
        teacherform=TeacherRegisterForm(
            request.POST, request.FILES)
        if userform.is_valid() and teacherform.is_valid():
            user = userform.save(commit=False)
            user.save()
            teacher = teacherform.save(commit=False)
            teacher.user = user
            teacher.save()
            username = userform.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('Login')
        else:
            print(userform.errors)
    else:
        userform = UserRegisterForm()
        teacherform = TeacherRegisterForm()
        context = {'form': userform, 'tform': teacherform}
        render(request,'TeacherSignup.html',context)

    
