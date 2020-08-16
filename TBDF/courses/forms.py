from django import forms
from courses.models import QuizSent

class QuizRegisterForm(forms.ModelForm):
    class Meta:
        model = QuizSent
        fields = ['mobile_number', 'description', 'answer_key', 'total_marks']
