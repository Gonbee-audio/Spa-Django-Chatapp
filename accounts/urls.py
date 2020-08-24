from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import AuthRegister

urlpatterns = [
    path('register/', AuthRegister.as_view(), name="signup"),
]