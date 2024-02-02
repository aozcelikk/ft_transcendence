from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.models import Kisiler,Kategori



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
			"kisiler":Kisiler.objects.all(),
			"kategoriler":Kategori.objects.all()
		}
		return render(request, "blog/kisiler.html", kullanici_veri)
	return render(request, "blog/index.html")

def kisiler_detay(request, slug):
	if request.user.is_authenticated:
		kullanici_veri = {
			"kisiler":Kisiler.objects.get(slug=slug),
			"kategoriler":Kategori.objects.all(),
			"secilen": slug
		}
		return render(request, "blog/kisiler_detay.html",{
			"slug": kullanici_veri["kisiler"],
			"kategoriler": kullanici_veri["kategoriler"],
			"secilen": kullanici_veri["secilen"]
		})
	return render(request, "blog/index.html")


def kisiler_kagetori(request, slug):
	if request.user.is_authenticated:
		bilgiler = {
			#"kisiler":Kisiler.objects.filter(kategori__slug=slug),
			"kisiler":Kategori.objects.get(slug=slug).kisiler_set.all(),
			"kategoriler":Kategori.objects.all(),
			"secilen": slug
		}
		return render(request, "blog/kisiler.html",bilgiler)
	return render(request, "blog/index.html")