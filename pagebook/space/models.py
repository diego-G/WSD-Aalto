from django.db import models
from django.forms import ModelForm

# Create your models here.
from django.contrib.auth.models import User

import datetime

class Image(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.URLField(blank=False)
    
    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    private = models.BooleanField()
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    def __unicode__(self):
        return self.name

class Page(models.Model):
    number = models.IntegerField()
    layout = models.IntegerField()
    images = models.ManyToManyField(Image)
    album = models.ForeignKey(Album)
    
    def __unicode__(self):
        return self.number

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        exclude = ('user')