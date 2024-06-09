# urls.py
from django.urls import path
from .views import EventListView, EventCreateView, rsvp_view, review_view
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('rsvp/<int:event_id>/', rsvp_view, name='rsvp'),
    path('review/<int:event_id>/', views.review_view, name='review'),
    path('review_success/', views.review_success, name='review_success'),
    path('rsvp/<int:event_id>/', views.rsvp_view, name='rsvp'),
    path('rsvp_success/', views.rsvp_success, name='rsvp_success'),
]
