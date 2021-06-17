from django.urls import re_path,path
from django.conf.urls import url
# from . import consumers
from .consumer import NSEConsumer

websocket_urlpatterns = [
    re_path('watchlist/$', NSEConsumer.as_asgi()),
]
