from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Answer, Tutor, Student, Assignment


class createUSerForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'
        exlude = ['slug',]

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'