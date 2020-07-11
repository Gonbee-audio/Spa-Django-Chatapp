# coding: utf-8

from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'chatmessage', views.ChatMessageViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'secredmessage', views.SecredMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]