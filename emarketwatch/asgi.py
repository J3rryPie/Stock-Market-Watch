
import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from watchlist.consumers import NSEConsumer
from channels.auth import AuthMiddlewareStack

application = get_asgi_application()

ws_patterns = [
    path('ws/test/' ,NSEConsumer.as_asgi() ),
    # path('ws/new/' , NewConsumer)
]

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(URLRouter(ws_patterns))
})
