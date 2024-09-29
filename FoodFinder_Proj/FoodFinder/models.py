import datetime
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    place_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    favorites = models.ManyToManyField(User, blank=True, related_name='restaurants', default=None)