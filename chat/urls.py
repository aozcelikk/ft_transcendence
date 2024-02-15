from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import translation
from django.urls import path


# urlpatterns = [
# 	path(_("anasayfa/"), views.sohbet_anasayfa, name="sohbet_anasayfa"),
# 	path(_("oyun_gecmis/"), views.game_history, name="oyun_gecmis"),
# 	path('update_winner/<room_name>', views.guncelleme, name='guncelleme'),
# 	path(_("<str:room_name>/"),views.sohbet_oda, name='oda'),
# ]

urlpatterns = [
	path(_("anasayfa/"), views.sohbet_anasayfa, name="sohbet_anasayfa"),
	path(_("oyun_gecmis/"), views.game_history, name="oyun_gecmis"),
    path('create_tournament/', views.create_tournament, name='create_tournament'),
    path('home/', views.home, name='home'),
    path('join_tournament/<int:tournament_id>/', views.join_tournament, name='join_tournament'),
	path('update_winner/<room_name>', views.guncelleme, name='guncelleme'),
	path(_("<str:room_name>/"),views.sohbet_oda, name='oda'),
]
