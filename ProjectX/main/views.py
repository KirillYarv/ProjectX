from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Teacher, TeacherProfile
from .auth import create_user
from .form import AuthForm, TeacherForm, AuthTeacherForm, LoginForm


# Create your views here.
def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')
def login(request):

    form = LoginForm()

    data = {'form': form}
    return render(request, 'registration/login.html',data)


def logout(request):
    return render(request, 'registration/logged_out.html')

def auth_teacher(request):
    error = ''
    a = ''
    if request.method == 'POST':
        form = AuthForm(request.POST)
        form_education = AuthTeacherForm(request.POST)

        if form.is_valid() and form_education.is_valid():
            create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            a = User.objects.all()
            form_teacher = Teacher(user=a[len(a) - 1], is_teacher=1)
            form_teacher_profile = TeacherProfile(user=a[len(a) - 1], education=form_education.cleaned_data['education'])

            form_teacher.save()
            form_teacher_profile.save()

            return redirect('../../../accounts/login/')
        else:
            error = "Форма не верна"
    form = AuthForm()
    form_education = AuthTeacherForm()
    data = {
        'form': form,
        'form_education': form_education,
        'error': error
    }
    return render(request, 'registration/Регистрация-для-репетитора.html', data)
def auth_student(request):
    error = ''
    a= ''
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            a = User.objects.all()
            form_teacher = Teacher(user = a[len(a)-1], is_teacher = 0)
            form_teacher.save()

            return redirect('../../../accounts/login/')
        else:
            error = "Форма не верна"
    form = AuthForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/Регистрация-для-обучающегося.html',data)
