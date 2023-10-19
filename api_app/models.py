from django.db import models

# Create your models here.
class CD(models.Model):
    album = models.TextField()
    artist = models.TextField()
    year = models.IntegerField()
