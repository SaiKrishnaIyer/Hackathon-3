# forms.py
from django import forms
from .models import Event, RSVP, Review

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'location', 'date', 'description']

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['event', 'user_name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['event', 'user_name', 'rating', 'comment']
