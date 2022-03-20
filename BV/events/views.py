from django.db.models import Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Enrollment, Review

events_list = Event.objects.all()

def hi(request):
    return HttpResponse('<h1>This page works</h1>')


def all_events(request):
    return render(request, 'events.html', {'events_list': events_list})


def enroll(request, event, slug):
    traveller = request.user
    mobile = '10165658599'
    Enrollment.objects.create(event=event, traveller=traveller, mobile=mobile)



def event_detail(request, slug=None):
    event = Event.objects.get(slug=slug)
    review = Review.objects.filter(event=event).count()
    rating = Review.objects.filter(event=event).aggregate(Avg('star'))
    if not request.user.is_authenticated:
        if request.method == 'POST':
            return redirect('/accounts/login/')
        if slug is not None:
            return render(request, 'event_single.html', {'event': event, 'slug': slug, 'event': event, 'review': review, 'rating': rating['star__avg'],'enrolled': False, 'events_list': events_list})
    else:
        enrolled = Enrollment.objects.filter(traveller=request.user, event=event).exists()
        if slug is not None:
            if request.method == 'POST':
                if enrolled:
                    return redirect('/events/'+slug)
                enroll(request, event, slug)
                return redirect('/events/' + slug)
            return render(request, 'event_single.html', {'event': event, 'slug': slug, 'event': event, 'review': review, 'rating': rating['star__avg'], 'enrolled': enrolled, 'events_list': events_list})
