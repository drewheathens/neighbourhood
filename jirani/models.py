from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt


# Create your models here.
class Profile(models.Model):
	name = models.TextField(max_length = 100)
	photo = models.ImageField(upload_to = 'profile/')
	profile = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
	bio = models.TextField(max_length = 100)
	contact = models.IntegerField()
	email = models.TextField(max_length = 50)

	def save_profile(self):
		self.save()

	def delete_profile(self):
		self.delete()

class Neighborhood(models.Model):
	neighborhood= models.CharField(max_length=100)

	def __str__(self):
		return self.neighborhood

	def save_neighborhood(self):
		self.save()

	@classmethod
	def delete_neighborhood(cls,neighborhood):
		cls.objects.filter(neighborhood=neighborhood).delete()

# class Category(models.Model):

class Business(models.Model):
	description = HTMLField()
	neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	name =models.CharField(max_length=100)
	email = models.EmailField()
	address =models.CharField(max_length=100)
	contact = models.IntegerField()

	def __str__(self):
		return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls,search_term):
        blogs = cls.objects.filter(Q(username__username=search_term) | Q(neighbourhood__neighbourhood=search_term) | Q(title__icontains=search_term))
        return blogs


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    # priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class medicalservices(models.Model):
    medicalservices = models.CharField(max_length=100)

    def __str__(self):
        return self.medicalservices

    def save_medicalservices(self):
        self.save()

    @classmethod
    def delete_medicalservices(cls,medicalservices):
        cls.objects.filter(medicalservices=medicalservices).delete()

class Health(models.Model):
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    medicalservices = models.ManyToManyField(medicalservices)

    def __str__(self):
        return self.name

class Security(models.Model):
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name


