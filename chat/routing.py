from django.urls import path
from .consumer import GameConsumer

websocket_urlpatterns = [
    path('ws/game/<room_code>', GameConsumer.as_asgi()),
]
