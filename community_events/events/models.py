# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255, default='Default Event Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return f"{self.user_name} - {self.event.name}"

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, default='Anonymous')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_name} - {self.event.name} - {self.rating}"
