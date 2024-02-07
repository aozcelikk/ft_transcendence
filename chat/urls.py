from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import translation
from django.urls import path
# from .views import game_history, tictac, play, update_winner

urlpatterns = [
	path(_("anasayfa/"), views.sohbet_anasayfa, name="sohbet_anasayfa"),
	path(_("<str:room_name>/"),views.sohbet_oda),
]

# urlpatterns = [
#     path('', tictac, name='tictac_create'),
#     path('<room_code>', play, name='play'),
#     path('history/', game_history, name='game_history'),
#     path('update_winner/<room_code>', update_winner, name='update_winner'),
# ]