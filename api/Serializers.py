from rest_framework import serializers
from .models import ChatMessage, Comment, SecredMessage
from accounts.models import User

class ChatMessageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('nickname', 'icon')

class CommentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('username', 'text','icon')


class SecredMessageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecredMessage
        fields = ('yourname', 'username', 'nickname','image', 'text', 'icon')

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'image')

