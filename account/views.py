from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


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
					"error": _("Kullanıcı adı yada parola yanlış")
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
		return render(request, "account/user_page.html")
	return redirect("anasayfa")

def logout_request(request):
	logout(request)
	return redirect("giris")
