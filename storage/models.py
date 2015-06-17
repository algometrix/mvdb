from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=40)
    cover_image=models.URLField(null=True)
    rating=models.IntegerField(null=True)
    size_mb=models.IntegerField(null=True)
    description=models.CharField(max_length=300)
    duration_min=models.IntegerField(null=True)
    screenshot_1=models.URLField(null=True)
    screenshot_2=models.URLField(null=True)
    genre=models.ManyToManyField('Genre',null=True)
    cast=models.ManyToManyField('Cast',null=True)
    
    def __unicode__(self):
        return self.name
        
class Link(models.Model):
    url=models.URLField(null=True)
    movie=models.ForeignKey('Movie',null=True)
    
class Genre(models.Model):
    name=models.CharField(max_length=40)
    
    
class Cast(models.Model):
    name=models.CharField(max_length=40)
    gender=models.CharField(max_length=6)
    
class Director(models.Model):
    name=models.CharField(max_length=40)
    