# admin.py
from django.contrib import admin
from .models import Category, Event, RSVP, Review

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(RSVP)
admin.site.register(Review)
