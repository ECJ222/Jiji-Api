from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	username = models.CharField(max_length = 100, unique = True, blank = True, null = True)
	state_of_residence = models.CharField(max_length = 255)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return '{}'.format(self.email)

class LoginUser(models.Model):
	email = models.EmailField(unique = True)
	password = models.CharField(max_length = 255)

	def __str__(self):
		return self.email

class Product(models.Model):
	seller = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
	name = models.CharField(max_length = 300)
	price = models.IntegerField()
	image = models.ImageField()
	description = models.CharField(max_length = 500)
	sold = models.BooleanField(default = False)

	def __str__(self):
		return self.name

class Buyer(models.Model):
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True, blank = True)
	name = models.CharField(max_length = 300)
	email = models.EmailField()
	location = models.CharField(max_length = 900)

	def __str__(self):
		return '{} {}'.format(self.name, self.location)

	