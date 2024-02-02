from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.text import slugify


from django.dispatch import receiver
from django.db.models.signals import post_save


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
	user = models.OneToOneField(User, on_delete= models.CASCADE )


	def __str__(self):
		return "{0}".format(self.user)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user)
		self.kullanici = self.user.username
		self.tam_adi = self.user.first_name + " " + self.user.last_name
		super().save(*args, **kwargs)

	@receiver(post_save, sender = User)
	def user_is_created(sender, instance, created, **kwargs):
		if created:
			Kisiler.objects.create(user= instance)
		else:
			instance.kisiler.save()


