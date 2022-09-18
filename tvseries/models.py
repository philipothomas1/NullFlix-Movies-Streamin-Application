from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
import datetime
# Create your models here.

LANGUAGE_CHOICES = [
	('ENGLISH', 'ENGLISH'),
	('FRENCH', 'FRENCH'),
	('SPANISH', 'SPANISH'),
	('ITALIANO', 'ITALIANO'),
	('CHINESE', 'CHINESE'),
	('JAPANESE', 'JAPANESE'),
	('RUSSIAN', 'RUSSIAN'),
	('SWAHILI', 'SWAHILI'),

]
GENRE_CHOICES = [
	('COMEDY', 'COMEDY'),
    ('SCI-FI', 'SCI-FI'),
	('ACTION', 'ACTION'),
	('ROMANCE', 'ROMANCE'),
	('ROMCOMEDY', 'ROMCOMEDY'),
	('ADVENTURE', 'ADVENTURE'),
	('DRAMA', 'DRAMA'),
	('HORROR', 'HORROR'),
    ('ANIMATION', 'ANIMATION'),

]


STATUS_CHOICES = [
	('IN PRODUCTION', 'IN PRODUCTION'),
	('ENDED', 'ENDED'),
	('CANCELLED', 'CANCELLED'),

]
QUALITY_CHOICES=[
	('1080HD','1080HD'),
	('720HD','720HD'),
	('480P','480P'),
	('3GP','3GP')
]
class TVSeries(models.Model):
    tv_series_name=models.CharField(max_length=100,blank=True,null=True)
    poster=models.ImageField(blank=True,null=True)
    status= models.CharField(choices=STATUS_CHOICES,max_length=100, blank=True,null=True)
    genre= models.CharField(choices=GENRE_CHOICES,max_length=100, blank=True,null=True)
    premiere = models.DateField(default=datetime.date.today,null=True)
    country = CountryField(blank=True,null=True)
    # added_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True,unique=True)
    

    class Meta:
        verbose_name_plural='TVSeries'

    def get_absolute_url(self):
        return reverse("movies:season_in_series", args=[self.slug])

    def __str__(self):
        return self.tv_series_name


class Season(models.Model):
    season_number=models.IntegerField(blank=True,null=True)
    tv_series=models.ForeignKey(TVSeries,on_delete=models.CASCADE,blank=True,null=True)
    
    slug = models.SlugField(null=True,blank=True,unique=True)
    def __str__(self):
        return str(self.season_number)
	

class Episode(models.Model):
    # tv_series_name=models.ForeignKey(TVSeries,on_delete=models.CASCADE,blank=True,null=True)
    episode_number=models.IntegerField(blank=True,null=True)
    episode_theme=models.CharField(blank=True,null=True,max_length=50)
    season=models.ForeignKey(Season,on_delete=models.CASCADE,blank=True,null=True)
    episode_video= models.FileField(upload_to='tvseries/episode_videos/', null=True, blank=True)
    quality=models.CharField(choices=QUALITY_CHOICES,max_length=20,blank=True,null=True)
    parental_gardian=models.IntegerField(blank=True,null=True)
    released = models.DateField(default=datetime.date.today,null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=300, blank=True,null=True)
    plot = models.TextField(max_length=1000, blank=True,null=True)

    def __str__(self):
        return str(self.episode_number)
