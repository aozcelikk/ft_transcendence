from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.db import models
from blog.models import Kisiler,Kategori
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import constants as messages
from .forms import ResimForm,KullaniciAyarForm


def login_request(request):
	if request.user.is_authenticated:
		return redirect("anasayfa")
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(request, username = username, password = password)
		
		if user is not None:
			login(request, user)
			return redirect("giris")
		else:
			return render(request, "account/login.html", {
					"error": _("Kullanıcı adı yada parola yanlış"),
					"kisiler":Kisiler.objects.all()
				})

	return render(request, "account/login.html")

def register_request(request):
	if request.user.is_authenticated:
		return redirect("anasayfa")

	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		firstname = request.POST["firstname"]
		lastname = request.POST["lastname"]
		password = request.POST["password"]
		repassword = request.POST["repassword"]

		if password == repassword:
			if User.objects.filter(username=username).exists():
				return render(request, "account/register.html", {
				"error": _("Kullanıcı adı bulunmakta!"),
				"username":username,
				"email":email,
				"firstname":firstname,
				"lastname":lastname
			})
			else:
				if User.objects.filter(email=email).exists():
					return render(request, "account/register.html", {
						"error": _("Email kullanılmakta!"),
						"username":username,
						"email":email,
						"firstname":firstname,
						"lastname":lastname
					})
				else:
					user = User.objects.create_user(username=username,email=email,
					first_name=firstname,last_name=lastname,password=password)
					user.save()
					return redirect("giris")
		else:
			return render(request, "account/register.html", {
				"error": _("Parola eşleşmiyor!"),
				"username":username,
				"email":email,
				"firstname":firstname,
				"lastname":lastname
			})

	return render(request, "account/register.html")


def auth_settings(request):
	if request.user.is_authenticated:
		veri={
			"kisiler":Kisiler.objects.all()
		}
		return render(request, "account/user_page.html", veri)
	return redirect("anasayfa")


def password_change(request):
	if request.user.is_authenticated:
		return render(request, "registration/password_change_form.html")
	return redirect("anasayfa")

def resim(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			form = ResimForm(request.POST, request.FILES, instance=request.user.kisiler)
			if form.is_valid():
				form.save()
				return redirect('kullanici')
			else:
				form = ResimForm(instance=request.user)
		else:
			form=ResimForm()
		return render(request, 'registration/resim.html', {'form': form})
	return redirect("anasayfa")

def kullan(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			form = KullaniciAyarForm(request.POST,instance=request.user)
			if form.is_valid():
				form.save()
				return redirect('kullanici')
			else:
				form = KullaniciAyarForm(instance=request.user)
		else:
			form=KullaniciAyarForm()
		return render(request, 'registration/kullan.html', {'form': form})
	return redirect("anasayfa")

def logout_request(request):
	logout(request)
	return redirect("giris")
