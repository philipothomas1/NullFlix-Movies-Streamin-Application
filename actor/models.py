from django.db import models

from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Actor(models.Model):
	name = models.CharField(max_length=70, unique=True)
	picture = models.ImageField(blank=True)
	slug = models.SlugField(null=True,blank=True,unique=True)	
	movies = models.ManyToManyField('movies.Movie')



	def __str__(self):
		return self.name

