from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    place_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites', default=None)

class Comment(models.Model):
   restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   text = models.TextField()
   profile_picture = models.URLField(max_length=200, blank=True, null=True)
   author_name = models.CharField(max_length=255)

   def __str__(self):
       return f'Comment by {self.user.username} on {self.restaurant.name}'
