import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsappapi.settings')
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application
  


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
