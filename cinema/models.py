from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='posters')
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    upload_time = models.TimeField(auto_now_add=True)
    favorites = models.ManyToManyField('account.CustomUser', related_name='favorite', blank=True)
    categories = models.ManyToManyField('Category')


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)



