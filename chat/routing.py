from django.urls import path,re_path
from .consumer import GameConsumer


websocket_urlpatterns = [
#    path('ws/game/<room_code>', GameConsumer.as_asgi()),
#	re_path(r"ws/sohbet/(?P<room_name>\w+)/$", GameConsumer.as_asgi()),
	path('ws/sohbet/<str:room_name>/', GameConsumer.as_asgi()),
]

