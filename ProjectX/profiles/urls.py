from django.urls import path

from . import views


urlpatterns = [

    path('', views.profile, name='profile'),
    path('chat/', views.chat, name='chat'),

]
