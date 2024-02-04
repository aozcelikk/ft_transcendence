from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.text import slugify



class Kisiler(models.Model):
	kullanici = models.CharField(max_length=150, null=False)
	tam_adi = models.CharField(max_length=150, null=False)
	resim = models.ImageField(upload_to="blogs", default="blogs/7.jpg", blank=True)
	toplam_mac = models.IntegerField(default=0)
	zafer_mac = models.IntegerField(default=0)
	bozgun_mac = models.IntegerField(default=0)
	engel = models.BooleanField(default=True)
	cevrimici = models.BooleanField(default=False)
	slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	friends = models.ManyToManyField(User, related_name="friends", blank=True)

	def get_friends(self):
		return self.friends.all()
	
	def get_friends_no(self):
		return self.friends.all().count()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.user)
		self.kullanici = self.user.username
		self.tam_adi = self.user.first_name + " " + self.user.last_name
		self.toplam_mac = self.zafer_mac + self.bozgun_mac
		super().save(*args, **kwargs)

	def __str__(self):
		return "{0}".format(self.user)

STATUS_CHOICES = (
	('send','send'),
	('accepted','accepted'),
)

class Relationship(models.Model):
	sender=models.ForeignKey(Kisiler, related_name='sender', on_delete=models.CASCADE)
	receiver=models.ForeignKey(Kisiler, related_name='receiver', on_delete=models.CASCADE)
	status=models.CharField(max_length=8, choices=STATUS_CHOICES)

	def __str__(self):
		return f"{self.sender}-{self.receiver}-{self.status}"
