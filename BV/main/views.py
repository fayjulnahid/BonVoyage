from events.models import Event
from django.shortcuts import render


def index(request):
    events_list=Event.objects.all().exclude(date=None)
    upcoming=Event.objects.filter(date=None).all()
    return render(request,'main/index.html',{'events_list': events_list, 'upcoming': upcoming})
# Create your views here.
