from django.urls import re_path
from api.consumers import *


websocket_urlpatterns = [
    re_path('/ws/', ChatConsumer.as_asgi()),
]

