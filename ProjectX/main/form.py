from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

from .models import Teacher, TeacherProfile


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['is_teacher']
class AuthForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'u-input u-input-rectangle',
                'placeholder': 'Пароль',
                'id': 'text-4495',
                'name': 'password',
            }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'u-input u-input-rectangle',
                'placeholder': 'Логин',
                'type': 'text',
                'id': 'name-6797',
                'name': 'name',
            }),
            "email": TextInput(attrs={
                'class': 'u-input u-input-rectangle',
                'placeholder': 'Почта',
                'type': 'email',
                'id': 'email-6797',
                'name': 'email',
            }),
            # "repeat_password": TextInput(attrs={
            #     'class': 'u-input u-input-rectangle',
            #     'placeholder': 'Логин',
            #     'type': 'text',
            #     'id': 'name-6797',
            #     'name': 'name',
            # })
        }
class AuthTeacherForm(ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['education']
        widgets = {
            "education": TextInput(attrs={
                'class': 'u-input u-input-rectangle',
                'placeholder': 'Ваше образование',
                'type': 'text',
                'id': 'text-527e',
                'name': 'education',
            })
        }