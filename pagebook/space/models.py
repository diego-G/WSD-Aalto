from django.db import models
from django import forms
from django.forms import ModelForm
from django.conf import Settings 

# Create your models here.
from django.contrib.auth.models import User

import datetime

class Image(models.Model):
    file = models.ImageField(upload_to='/media/')
    
    def __unicode__(self):
        return self.file

class Album(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    private = models.BooleanField()
    
    
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    def __unicode__(self):
        return self.id

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

class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('album','images','number')
        
class ImageForm(ModelForm):
    class Meta:
        model = Image