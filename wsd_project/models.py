from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    description = models.CharField(max_length=255)
    url = models.URLField(blank=False)

class Album(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    private = models.BooleanField()

class Page(models.Model):
    number = models.IntegerField()
    layout = models.IntegerField()
    images = models.ManyToManyField(Image)
    album = models.ForeignKey(Album)
