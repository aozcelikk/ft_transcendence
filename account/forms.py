from django import forms
from blog.models import Kisiler
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class ResimForm(forms.ModelForm):
	class Meta:
		model = Kisiler
		fields = ['resim']

class KullaniciAyarForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

