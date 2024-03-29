from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Kisiler,Relationship

@receiver(post_save, sender=User)
def post_save_create_blog(sender, instance, created, **kwargs):
	if created:
		Kisiler.objects.create(user=instance)
	else:
		instance.kisiler.save()

@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
	sender_=instance.sender
	receiver_=instance.receiver
	if instance.status=='accepted':
		sender_.friends.add(receiver_.user)
		receiver_.friends.add(sender_.user)
		sender_.save()
		receiver_.save()