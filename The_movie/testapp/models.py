from django.db import models

# Create your models here.

class movie(models.Model):
    rdate = models.DateField()
    moviename = models.CharField(max_length=30)
    hero = models.CharField(max_length=30)
    heroiene = models.CharField(max_length=30)
    rating = models.IntegerField()

    