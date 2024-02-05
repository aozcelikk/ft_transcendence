from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.models import Kisiler,Arkadas
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

def arkadaslar(request):
	if request.user.is_authenticated:
		users=User.objects.exclude(id=request.user.id)
		veri_depo = {}
		veri_depo['users']=users
		veri_depo['kisiler']=Kisiler.objects.all()
		veri_depo['engel']=Arkadas.objects.all()
		ark=Arkadas.objects.filter(diger_users=request.user)
		if len(ark)>0:
			arkadas=Arkadas.objects.get(diger_users=request.user)
			arkadaslar = arkadas.users.all()
			veri_depo['arkadaslar']=arkadaslar
		return render(request, "blog/part/_arkadas.html", veri_depo)
	return render(request, "blog/index.html")


def kisiler(request):
	if request.user.is_authenticated:
		users=Kisiler.objects.exclude(id=request.user.id)
		veri_depo = {}
		veri_depo['users']=users
		return render(request, "blog/kisiler.html", veri_depo)
	return render(request, "blog/index.html")


def cevrimici(request):
	if request.user.is_authenticated:
		users=Kisiler.objects.exclude(id=request.user.id)
		veri_depo = {}
		veri_depo['users']=users
		ark=Arkadas.objects.get(diger_users=request.user)
		arkadaslar = ark.users.all()
		veri_depo['arkadaslar']=arkadaslar
		return render(request, "blog/part/_cevrimici.html", veri_depo)
	return render(request, "blog/index.html")

def arkadas_sistem(request, alternatif, pk, engel):
	arkadas = User.objects.get(pk=pk)
	users=request.user
	if alternatif == 'ekle':
		Arkadas.arkadas_ekle(request.user, arkadas, engel)
	elif alternatif == 'sil':
		Arkadas.arkadas_sil(request.user, arkadas, engel)
	elif alternatif == 'engelle':
		Arkadas.arkadas_engelle(request.user,arkadas, engel)
	elif alternatif == 'kaldir':
		Arkadas.arkadas_kaldir(request.user,arkadas, engel)
	return redirect('kisiler')

