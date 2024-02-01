from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

# Create your views here.

def sohbet_anasayfa(request):
    if request.user.is_authenticated:
        return render(request, "sohbet_anasayfa.html")
    return redirect("ilksayfa")

def sohbet_oda(request,room_name):
    if request.user.is_authenticated:
        return render(request,"oda.html",{"roomname":room_name})
    return redirect("ilksayfa")