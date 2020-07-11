from django.contrib import admin
from .models import ChatMessage, Comment, SecredMessage

admin.site.register(ChatMessage)
admin.site.register(Comment)
admin.site.register(SecredMessage)
