from rest_framework import serializers
from .models import ChatMessage, Comment, SecredMessage
from accounts.models import User

class ChatMessageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = ('id', 'nickname', 'icon', 'text', 'username')

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('username', 'text','icon')


class SecredMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecredMessage
        fields = ('yourname', 'username', 'nickname','image', 'text', 'icon')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'password', 'image')

