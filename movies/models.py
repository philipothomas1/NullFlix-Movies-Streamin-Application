from django.db import models
from actor.models import Actor

from django.utils.text import slugify
# import requests
from io import BytesIO
from django.core import files
from django.urls import reverse

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



LANGUAGE_CHOICES = [
	('EN', 'ENGLISH'),
	('FR', 'FRENCH'),
	('SP', 'SPANISH'),
	('IT', 'ITALIANO'),
	('CHN', 'CHINESE'),
	('JPN', 'JAPANESE'),
	('RS', 'RUSSIAN'),
	('SW', 'SWAHILI'),

]
GENRE_CHOICES = [
	('COMEDY', 'COMEDY'),
	('ACTION', 'ACTION'),
	('ROM', 'ROMANCE'),
	('ROMCOM', 'ROMCOMEDY'),
	('ADV', 'ADVENTURE'),
	('DRM', 'DRAMA'),
	('HR', 'HORROR'),
	

]
QUALITY_CHOICES=[
	('1080HD','1080HD'),
	('720HD','720HD'),
	('480P','480P'),
	('3GP','3GP')
]
class MovieGenre(models.Model):
	genre_name = models.CharField(max_length=25)
	slug = models.SlugField(verbose_name=_("Category safe URL"),null=True,unique=True)
# 	# slug = models.SlugField(null=False, unique=True)

	def get_absolute_url(self):
		return reverse("movies:movies_in_genre", args=[self.slug])


	def __str__(self):
		return self.genre_name

	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		self.title.replace(" ", "")
	# 		self.slug = slugify(self.title)
	# 	return super().save(*args, **kwargs)

# class Rating(models.Model):
# 	source = models.CharField(max_length=50)
# 	rating = models.CharField(max_length=10)

# 	def __str__(self):
# 		return self.source

class Movie(models.Model):
	Title = models.CharField(max_length=200)
	Year = models.DateField()
	# Rated = models.CharField(max_length=10, blank=True)
	Released = models.DateField()
	Description = models.TextField(max_length=1000, blank=True)
	genre = models.ForeignKey(MovieGenre,on_delete=models.CASCADE,max_length=300, blank=True,null=True)
	Director = models.CharField(max_length=100, blank=True)
	Writer = models.CharField(max_length=300, blank=True)
	Actors = models.ManyToManyField(Actor, blank=True)
	Plot = models.CharField(max_length=900, blank=True)
	Language = models.CharField(choices=LANGUAGE_CHOICES,max_length=300, blank=True)
	Country = models.CharField(max_length=100, blank=True)
	#Awards = models.CharField(max_length=250, blank=True)
	Poster = models.ImageField(upload_to='movies', blank=True)
	slug = models.SlugField(null=True, blank=True)
	added_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	# Poster_url = models.URLField(blank=True)
	# Ratings = models.ManyToManyField(Rating, blank=True)
	# status = models.CharField(max_length=5, blank=True)
	# imdbRating = models.CharField(max_length=5, blank=True)
	# imdbVotes = models.CharField(max_length=100, blank=True)
	# imdbID = models.CharField(max_length=100, blank=True)
	# Type = models.CharField(max_length=10, blank=True)
	# DVD = models.CharField(max_length=25, blank=True)
	# BoxOffice = models.CharField(max_length=25, blank=True)
	# Production = models.CharField(max_length=100, blank=True)
	# Website = models.CharField(max_length=150, blank=True)
	# totalSeasons = models.CharField(max_length=3, blank=True)
	quality=models.CharField(choices=QUALITY_CHOICES,max_length=20,blank=True,null=True)
	parental_gardian=models.IntegerField(blank=True,null=True)
	# movie_trailer=models.URLField(blank=True,null=True)
	movie_trailer= models.FileField(upload_to='movies/videos/trailers', null=True, blank=True)
	def save(self, *args, **kwargs):
		if  not self.slug:
			self.slug=slugify(self.Title)
		super(Movie,self).save(*args, **kwargs)

	def __str__(self):
		return self.Title

RATE_CHOICES = [
	(1, '1 - Trash'),
	(2, '2 - Horrible'),
	(3, '3 - Terrible'),
	(4, '4 - Bad'),
	(5, '5 - OK'),
	(6, '6 - Watchable'),
	(7, '7 - Good'),
	(8, '8 - Very Good'),
	(9, '9 - Perfect'),
	(10, '10 - Master Piece'), 
]
class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=3000, blank=True)
	rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
	likes = models.PositiveIntegerField(default=0)
	unlikes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.user.username


# class TVSeries(models.Model):
# 	tv_series_name=models.CharField(max_length=100,blank=True,null=True)

# 	class Meta:
# 		verbose_name_plural='TVSeries'

# 	def __str__(self):
# 		return self.tv_series_name


# class Season(models.Model):
# 	season=models.IntegerField(blank=True,null=True)
# 	tv_series=models.ForeignKey(TVSeries,on_delete=models.CASCADE,blank=True,null=True)
# 	def __str__(self):
# 		return str(self.season)
	

# class Episode(models.Model):
# 	tv_series_name=models.ForeignKey(TVSeries,on_delete=models.CASCADE,blank=True,null=True)
# 	episode_number=models.IntegerField(blank=True,null=True)
# 	episode_theme=models.CharField(blank=True,null=True,max_length=50)
# 	season=models.ForeignKey(Season,on_delete=models.CASCADE,blank=True,null=True)
# 	def __str__(self):
# 		return str(self.episode_number)


	


	

class SubPlan(models.Model):
	title=models.CharField(max_length=150)
	subprice=models.IntegerField()
	# max_member=models.IntegerField(null=True)
	highlight_status=models.BooleanField(default=False,null=True)
	validity_days=models.IntegerField(null=True)

	def __str__(self):
		return self.title

class SubPlanFeature(models.Model):
	# subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
	subplan=models.ManyToManyField(SubPlan)
	title=models.CharField(max_length=150)

	def __str__(self):
		return self.title


class SubPlanDiscount(models.Model):
	subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
	total_months=models.IntegerField()
	total_discount=models.IntegerField()

	def __str__(self):
		return str(self.total_months)

class Subscription(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	plan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
	price=models.CharField(max_length=50)
	reg_date=models.DateField(auto_now_add=True,null=True)

	def __str__(self):
		return str(self.user)

