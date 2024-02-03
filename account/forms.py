from django import forms
from blog.models import Kisiler,Kategori


class ImageForm(forms.ModelForm):
    class Meta:
        model = Kisiler
        fields = ('kullanici', 'tam_adi', 'resim', 'toplam_mac', 'zafer_mac', 'bozgun_mac', 'engel', 'cevrimici', 'kategoriler', 'user')