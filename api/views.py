import django_filters
from rest_framework import viewsets, filters

from .models import ChatMessage, Comment, SecredMessage
from accounts.models import User
from .Serializers import UserSerializers, CommentSerializers, SecredMessageSerializers, ChatMessageSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializers

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

class SecredMessageViewSet(viewsets.ModelViewSet):
    queryset = SecredMessage.objects.all()
    serializer_class = SecredMessageSerializers