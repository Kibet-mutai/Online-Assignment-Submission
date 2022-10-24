from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Answer, Tutor, Student, Assignment, User


class LoginForm(forms.Form):
    username =forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class SignupForm(UserCreationForm):
    username =forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2', 'is_admin', 'is_tutor', 'is_student']



class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'
        exlude = ['slug',]

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'