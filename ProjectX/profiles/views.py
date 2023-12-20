from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from main.models import Teacher

from .form import Chat
from .models import message, with_talker

def get_users():
    teachers = []
    students = []
    for i in Teacher.objects.all():
        for j in User.objects.all():
            if j.id == i.user_id:
                if i.is_teacher == '0':
                    students.append(j)
                else:
                    teachers.append(j)
    return (teachers,students)
@login_required
def profile(request):
    a = ''
    teachers, students = get_users()

    data = {
        'teachers': teachers,
        'students': students,
    }
    for i in Teacher.objects.all():
        if request.user.id == i.user_id:
            if i.is_teacher == '0':
                return render(request, 'profile/layout_profile_student.html', data)
            else:
                return render(request, 'profile/layout_profile_teacher.html', data)

@login_required
def chat(request):
    error = ''
    username = ''
    talk_username = ''
    teachers, students = get_users()

    #____________________________________
    if request.POST.get('talker'):
        try:
            with_talker.objects.filter(user_id=request.user.id).delete()
            form_with_talker = with_talker(talk_username=request.POST.get('talker'), user=request.user)
            form_with_talker.save()
        except:
            print()
    # ____________________________________
    # ____________________________________
    for i in with_talker.objects.all():
        if request.user.id == i.user_id:
            talk_username = i.talk_username
            break
    # ____________________________________
    text = []
    # ____________________________________
    if request.method == 'POST':
        if not request.POST.get('talker'):
            form = Chat(request.POST)
            form.is_valid()
            for i in User.objects.all():
                if request.user.id == i.id:
                    form_chat = message(username=i.username,talk_username = talk_username, text=form.cleaned_data['text'])
                    form_chat.save()
                    break
    # ____________________________________
    # ____________________________________
    form = Chat()
    text.clear()
    username = request.user.username
    for i in message.objects.all():
        if ((username == i.username and talk_username == i.talk_username) or
                (talk_username == i.username and username == i.talk_username)):
            text.append(i)
    # ____________________________________
    data = {
        'form': form,
        'username': username,
        'talk_username': talk_username,
        'text': text,
        'error': error,
        'teachers': teachers,
        'students': students,
    }


    for i in Teacher.objects.all():
        if request.user.id == i.user_id:

            if i.is_teacher == '0':
                return render(request, 'profile/chat_student.html', data)
            else:
                return render(request, 'profile/chat_teacher.html', data)
