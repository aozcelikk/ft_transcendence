from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _
from django.urls import path

urlpatterns = [
	path(_("anasayfa/"), views.sohbet_anasayfa, name="sohbet_anasayfa"),
	path(_("oyun_gecmis/"), views.game_history, name="oyun_gecmis"),
	path('turnuva/', views.turnuva, name='turnuva'),
	path('update_winner/<room_name>', views.guncelleme, name='guncelleme'),
	path(_("<str:room_name>/"),views.sohbet_oda, name='oda'),
	path('anasayfa/fetch-rooms/', views.fetch_rooms, name='fetch_rooms'),
]
