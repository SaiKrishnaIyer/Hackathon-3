# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Event, Category, RSVP, Review
from django.views.generic import ListView, CreateView
from .forms import EventForm, RSVPForm, ReviewForm
from django.http import HttpResponse

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse('event_list'))

def rsvp_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')

        if user_name and email:
            rsvp = RSVP.objects.create(event=event, user_name=user_name, email=email)
            rsvp.save()
            return redirect('rsvp_success')
        
        return render(request, 'events/rsvp_form.html', {'event': event, 'error': 'All fields are required.'})
    else:
        return render(request, 'events/rsvp_form.html', {'event': event})

def rsvp_success(request):
    return render(request, 'events/rsvp_success.html')

def rsvp_success(request):
    return render(request, 'events/rsvp_success.html')
from django.shortcuts import render, get_object_or_404
from .models import Event

def review_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if user_name and rating:
            review = Review.objects.create(event=event, user_name=user_name, rating=rating, comment=comment)
            review.save()
            # Redirect to the success page
            return redirect('review_success')
        
        # Handle case where form data is missing
        return render(request, 'events/review_form.html', {'event': event, 'error': 'All fields are required.'})
    else:
        return render(request, 'events/review_form.html', {'event': event})

def review_success(request):
    return render(request, 'events/review_success.html')

