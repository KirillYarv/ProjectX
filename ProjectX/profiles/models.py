from django.contrib.auth.models import User
from django.db import models

class message(models.Model):
    username = models.CharField(max_length=20)
    talk_username = models.CharField(max_length=20)
    text = models.TextField()
class with_talker(models.Model):
    talk_username = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
