from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView

urlpatterns = [
    path('register/', AuthRegister.as_view(), name="signup"),
    path('mypage/', AuthInfoGetView.as_view()),
]