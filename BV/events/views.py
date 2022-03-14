from django.shortcuts import render
from django.http import HttpResponse
from .models import Event


def hi(request):
    return HttpResponse('<h1>This page works</h1>')


def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'events.html', {'events_list': events_list})

