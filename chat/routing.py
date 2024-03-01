from django.urls import path,re_path
from .consumer import GameConsumer,SohbetAnasayfaConsumer


websocket_urlpatterns = [
	path('ws/sohbet/anasayfa/', SohbetAnasayfaConsumer.as_asgi()),
	path('ws/sohbet/<str:room_name>/', GameConsumer.as_asgi()),
]

