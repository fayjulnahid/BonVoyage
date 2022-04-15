from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from events.models import Event
from django.shortcuts import render
from . import forms
from .models import userProfile


def index(request):
    events_list=Event.objects.all().exclude(date=None)
    upcoming=Event.objects.filter(date=None).all()
    return render(request,'main/index.html',{'events_list': events_list, 'upcoming': upcoming})
# Create your views here.

@login_required(login_url="/accounts/login/")
def UserProfile(request):
    primaryKey = request.POST.get('primaryKey')
    if primaryKey is None:
        primaryKey = 3
    instance = userProfile.objects.get(id=primaryKey)
    UserProfile.user_name = request.POST.get('user_name')
    UserProfile.phone = request.POST.get('phone_number')
    UserProfile.address = request.POST.get('address')
    UserProfile.bio = request.POST.get('bio')
    UserProfile.image = request.FILES.get('image')

    if UserProfile.user_name is not None and UserProfile.user_name != '':
        instance.user_name = UserProfile.user_name

    if UserProfile.phone is not None and UserProfile.phone != '':
        instance.user_phone = UserProfile.phone

    if UserProfile.address is not None and UserProfile.address != '':
        instance.user_address = UserProfile.address

    if UserProfile.bio is not None and UserProfile.bio!= '':
        instance.bio = UserProfile.bio

    if UserProfile.image is not None:
        instance.user_image = UserProfile.image
    instance.save()

    profile = userProfile.objects.all()
    profile2 = userProfile.objects.filter(user=request.user).first()
    b = ''
    if profile2 is None:
        b = 'NoData'

    context = {}
    context['profile'] = profile
    context['booli'] = b
    context['name'] = UserProfile.user_name
    context['phone'] = UserProfile.phone
    context['address'] = UserProfile.address
    context['bio'] = UserProfile.bio
    context['image'] = UserProfile.image

    #userBookedHotels = HotelReservation.objects.filter(user=request.user)
    #context['userBookedHotels'] = userBookedHotels

    #reservation = HotelReservation.objects.filter(user=request.user)
    #count = 0
    #for i in reservation:
       # count += 1

    #context['offer'] = '0'
    #if 3 <= count < 5:
    #    context['offer'] = '30'
    #elif 5 <= count < 10:
    #    context['offer'] = '40'
    #elif count >= 10:
    #    context['offer'] = '50'

    return render(request, 'main/user_profile.html', context)


@login_required(login_url="/accounts/login/")
def createProfile(request):
    form = forms.UserProfile()
    if request.method == 'POST':
        form = forms.UserProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = forms.UserProfile()
    return render(request, 'main/createprofile.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')
