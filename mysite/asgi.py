"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

asgiapplication = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": asgiapplication,
        "websocket" : AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
    }
)

# Url yönlendirici, bağlantının http yolunu inceleyerek sağlanan url modeline göre 
# belirli bir alıcıya yönlendirir

# AuthMiddlewareStack, bağlantının kapsamını o anda kimliği doğrulanmış 
# kullanıcıya bir referansla dolduracaktır ,(django'nun isteğine benzer)

# ProtocolTypeRouter - bağlantı türünü inceler, eğer bir  websocket bağlantısı 
# ise (ws:// veya wss://) o zaman bağlantı AuthMiddlewareStack'e verilecektir