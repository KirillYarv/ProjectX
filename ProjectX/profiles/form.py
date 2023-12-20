from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

from .models import message


class Chat(ModelForm):
    class Meta:
        model = message
        fields = ['username', 'text']
        widgets = {
            "text": TextInput(attrs={
                'class': 'u-input u-input-rectangle',
                'placeholder': 'Ваше сообщение',
                'type': 'text',
                'id': 'text-527e',
                'name': 'text',
            })
        }