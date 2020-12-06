from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.

class ChatMessage(models.Model):
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images',blank=True, null=True)
    icon =models.CharField(max_length=1000)
    good = models.IntegerField(null=True, blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.username

class Comment(models.Model):
    chatmessage = models.ForeignKey(ChatMessage, on_delete=models.CASCADE, related_name='items')
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    icon =models.CharField(max_length=1000)
    
    def __str__(self):
        return self.text

class SecredMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usersend')
    username = models.CharField(max_length=30)
    yourname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    icon =models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username