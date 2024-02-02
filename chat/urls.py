from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import translation

urlpatterns = [
	path(_("anasayfa/"), views.sohbet_anasayfa, name="sohbet_anasayfa"),
	path(_("<str:room_name>/"),views.sohbet_oda),
]