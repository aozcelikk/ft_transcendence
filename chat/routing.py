from django.urls import path,re_path
from .consumer import GameConsumer,RoomConsumer,SohbetAnasayfaConsumer


websocket_urlpatterns = [
	path('ws/rooms/', RoomConsumer.as_asgi()),
	path('ws/anasayfa/', SohbetAnasayfaConsumer.as_asgi()),
	path('ws/sohbet/<str:room_name>/', GameConsumer.as_asgi()),
]


