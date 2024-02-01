from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from chat.consumer import Chating
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns
from django.utils import translation
from django.urls import re_path


websocket_urlpatterns = [
	re_path(r"ws/sohbet/(?P<room_name>\w+)/$", Chating.as_asgi()),
]
