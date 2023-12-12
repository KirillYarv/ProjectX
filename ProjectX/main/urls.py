from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/auth/teacher', views.auth_teacher, name='auth_teacher'),
    path('accounts/auth/student', views.auth_student, name='auth_student'),
    path('profile', views.profile, name='profile'),

]
