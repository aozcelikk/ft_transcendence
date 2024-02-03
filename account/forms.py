from django import forms
from blog.models import Kisiler,Kategori
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class ImageForm(forms.ModelForm):
	class Meta:
		model = Kisiler
		fields = ['resim']
