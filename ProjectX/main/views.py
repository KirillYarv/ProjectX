from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    data = {
        'title': 'Главная',
        'values': ['Book 1', 'Book 2', 'Book 3']
    }
    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')
def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logged_out.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')
def auth_teacher(request):
    return render(request, 'main/Регистрация-для-репетитора.html')
def auth_student(request):
    return render(request, 'main/Регистрация-для-обучающегося.html')
