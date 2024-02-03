from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
	class Meta:
		model=Image
		fields=('kullanici','tam_adi','resim','toplam_mac','zafer_mac','bozgun_mac','engel','cevrimici','slug','kategoriler','user')
		labels={
			'kullanici': '',
			'tam_adi': '',
			'resim': '',
			'toplam_mac': '',
			'zafer_mac': '',
			'bozgun_mac': '',
			'engel': '',
			'cevrimici': '',
			'slug': '',
			'kategoriler': '',
			'user': '',
		}