from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    place_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites', default=None)

class Apple(models.Model):
    name = models.CharField(max_length=255)