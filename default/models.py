from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class Todolist(models.Model):
    ip = models.CharField(default="",max_length=16)
    state = models.IntegerField(default=0)

class historydata(models.Model):
    ip = models.CharField(default="",max_length=16)
    time = models.IntegerField(default=time.time())
    state = models.IntegerField(default=0)