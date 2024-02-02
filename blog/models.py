from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class kisiler():
	username = models.CharField(max_length=1000, null=False)
	full_name = models.CharField(max_length=1000, null=False)
	picture = models.CharField(max_length=50, null=False)
	is_active = models.BooleanField(default=False)