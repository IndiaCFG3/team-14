from django.shortcuts import render
from django.http import request, HttpResponse

from django.contrib import messages

# Create your views here.


from accounts.models import Teacher
from courses.models import Student, QuizSent

from accounts.forms import UserRegisterForm, TeacherRegisterForm
from courses.forms import QuizRegisterForm

from twillio_send import send_sms



def home(request):

    return render(request, "landing.html")


def TeacherSignup(request):

    if request.method == 'POST':
        userform = UserRegisterForm(
            request.POST, request.FILES)
        teacherform = TeacherRegisterForm(
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
        return render(request, 'TeacherSignup.html', context)


def QuizSignup(request):
    if request.method == 'POST':
        Quizform = QuizRegisterForm(
            request.POST, request.FILES)


        #send_sms() yet to be implemented
        x = request.POST.get('description')
        send_sms(x)
        return HttpResponse('Quiz Sent!')
    else:
        quizform = QuizRegisterForm()
        context = {'form': quizform}
        return render(request, 'Quiz.html', context)


def DashBoard(request):

    teacher = Teacher.objects.get(user=request.user)

    students = Student.objects.all()

    context = {
        'teacher': teacher,
        'students': students
    }

    return render(request, 'dashBoard.html', context=context)


def chatbot(request):

    return HttpResponse("hello")


def SendSms(request):
    return render(request, "send_sms.html")
