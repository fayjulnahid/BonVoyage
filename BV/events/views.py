from django.db.models import Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Enrollment, Review

events_list = Event.objects.all()


def hi(request):
    return HttpResponse('<h1>This page works</h1>')


def all_events(request):
    return render(request, 'events.html', {'events_list': events_list})


def enroll(request, event):
    traveller = request.user
    mobile = '10165658599'
    Enrollment.objects.create(event=event, traveller=traveller, mobile=mobile)


def event_detail(request, slug=None):
    event = Event.objects.get(slug=slug)
    rating = Review.objects.filter(event=event).aggregate(Avg('star'))
    reviews = Review.objects.filter(event=event).count()
    if not request.user.is_authenticated:
        if slug is not None:
            event = Event.objects.get(slug=slug)
            if request.method == 'POST':
                return redirect('/accounts/login/')
        return render(request, 'event_single.html', {'events_list': events_list, 'event': event, 'slug': slug, 'rating': rating['star__avg'], 'reviews': reviews})
    else:

        enrolled = Enrollment.objects.filter(traveller=request.user, event=Event.objects.get(slug=slug)).exists()
        if slug is not None:
            event = Event.objects.get(slug=slug)
            if request.method == 'POST':
                enroll(request, event)
                return redirect('/events/' + event.slug)
        return render(request, 'event_single.html', {'events_list': events_list, 'event': event, 'slug': slug, 'enrolled': enrolled, 'rating': rating['star__avg'], 'reviews': reviews})
