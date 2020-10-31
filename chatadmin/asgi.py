# coding: utf-8
import os
import django
from channels.routing import get_default_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from chatadmin.routing import websocket_urlpatterns
# import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatadmin.settings")
django.setup()

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})


# application = get_default_application()

# channel_layer = channels.asgi.get_channel_layer()