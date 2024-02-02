from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


data = {
	"hepsi":User.objects.all()
}

def error_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
	if request.user.is_authenticated:
		return render(request, "blog/indexOO.html")
	return render(request, "blog/index.html")

def indexOO(request):
	if request.user.is_authenticated:
		return render(request, "blog/indexOO.html")
	return render(request, "blog/index.html")

def pingpong(request):
	if request.user.is_authenticated:
		return render(request, "blog/pingpong.html")
	return render(request, "blog/index.html")


def kisiler(request):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":data["hepsi"]
		}
		return render(request, "blog/kisiler.html", kullanici_veri)
	return render(request, "blog/index.html")

def kisiler_detay(request, id):
	if request.user.is_authenticated:
		return render(request, "blog/kisiler_detay.html",{
			"id": id
		})
	return render(request, "blog/index.html")