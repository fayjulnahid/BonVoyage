from events.models import Event
from django.shortcuts import render


def index(request):
    events_list=Event.objects.all()
    return render(request,'main/index.html',{'events_list': events_list})
# Create your views here.
