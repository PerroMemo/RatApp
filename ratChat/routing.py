from django.urls import path

from . import consumer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumer.ChatConsumer.as_asgi()),
]