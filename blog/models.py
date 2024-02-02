from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class kisiler(models.Model):
	kullanici = models.CharField(max_length=1000, null=False)
	tam_adi = models.CharField(max_length=1000, null=False)
	resim = models.CharField(max_length=50, null=False)
	toplam_mac = models.IntegerField(default=0)
	zafer_mac = models.IntegerField(default=0)
	bozgun_mac = models.IntegerField(default=0)
	cevrimici = models.BooleanField(default=False)