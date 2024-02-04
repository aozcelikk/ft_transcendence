from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.models import Kisiler
from account.forms import ResimForm,KullaniciAyarForm

def error_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
	if request.user.is_authenticated:
		return render(request, "blog/indexOO.html")
	return render(request, "blog/index.html")

def indexOO(request):
	user = request.user
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.all(),
		}
		return render(request, "blog/indexOO.html", kullanici_veri)
	return render(request, "blog/index.html")

def pingpong(request):
	if request.user.is_authenticated:
		return render(request, "blog/pingpong.html")
	return render(request, "blog/index.html")

def kisiler(request):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.all(),
		}
		return render(request, "blog/kisiler.html", kullanici_veri)
	return render(request, "blog/index.html")

def cevrimici(request):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.all(),
		}
		return render(request, "blog/part/_cevrimici.html", kullanici_veri)
	return render(request, "blog/index.html")

def arkadaslar(request):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.all(),
		}
		return render(request, "blog/part/_arkadas.html", kullanici_veri)
	return render(request, "blog/index.html")

def engellenenler(request):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.all(),
		}
		return render(request, "blog/part/_engellenenler.html", kullanici_veri)
	return render(request, "blog/index.html")

def kisiler_detay(request, slug):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.get(slug=slug),
		}
		return render(request, "blog/kisiler_detay.html",{
			"slug": kullanici_veri["kisiler"],
		})
	return render(request, "blog/index.html")
