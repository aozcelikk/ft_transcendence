from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


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

