from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.text import slugify



# class Kisiler(models.Model):
# 	kullanici = models.CharField(max_length=1000, null=False)
# 	tam_adi = models.CharField(max_length=1000, null=False)
# 	resim = models.ImageField(upload_to="blogs", default="blog/img/7.jpg")
# 	toplam_mac = models.IntegerField(default=0)
# 	zafer_mac = models.IntegerField(default=0)
# 	bozgun_mac = models.IntegerField(default=0)
# 	cevrimici = models.BooleanField(default=False)



class Kategori(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name
	


class Kisiler(models.Model):
	kullanici = models.CharField(max_length=150, null=False)
	tam_adi = models.CharField(max_length=150, null=False)
	resim = models.ImageField(upload_to="blogs", default="blog/img/7.jpg")
	toplam_mac = models.IntegerField(default=0)
	zafer_mac = models.IntegerField(default=0)
	bozgun_mac = models.IntegerField(default=0)
	engel = models.BooleanField(default=True)
	cevrimici = models.BooleanField(default=False)
	slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)
	kategoriler = models.ManyToManyField(Kategori, blank=True)


	def __str__(self):
		return f"{self.kullanici}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.kullanici)
		super().save(*args, **kwargs)


