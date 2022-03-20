from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Enrollment

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
    if not request.user.is_authenticated:
        if slug is not None:
            event = Event.objects.get(slug=slug)
        return render(request, 'event_single.html', {'event': event, 'slug': slug})
    else:
        if slug is not None:
            event = Event.objects.get(slug=slug)
            if request.method == 'POST':
                enroll(request, event)

        return render(request, 'event_single.html', {'event': event, 'slug': slug})
