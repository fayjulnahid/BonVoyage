import io

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from events.models import Event
from django.shortcuts import render, redirect
from . import forms
from .models import userProfile, HotelReview, RoomModel

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

from django.core.mail import send_mail
from . import forms


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

@login_required(login_url="/account/login/")
def RoomShow(request):
    hotelReview = HotelReview.objects.all().order_by('date')
    roomModel = RoomModel.objects.all().order_by('slug')
    profile = userProfile.objects.all()
    context = {}
    hotel_name = request.POST.get('hotel-name')
    context['hotel_name'] = hotel_name
    context['roomModel'] = roomModel
    context['profile'] = profile

    context['hotelReview'] = hotelReview

    hotel = hotel_name.split('_')
    mylist = ' '.join(hotel)
    context['mylist'] = mylist

    return render(request, 'main/HotelRoom.html', context)

@login_required(login_url="/account/login/")
def hotel_page(request):
    return render(request, 'main/HotelPage.html')

@login_required(login_url="/account/login/")
def hotelReview(request):
    form = forms.HotelReview()
    if request.method == 'POST':
        form = forms.HotelReview(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = forms.HotelReview()
    return render(request, 'main/HotelReview.html', {'form': form})


@login_required(login_url="/account/login/")
def deleteHotelReview(request, pk):
    instance = HotelReview.objects.get(id=pk)
    instance.delete()
    return redirect('articles:hotel_page')

@login_required(login_url="/account/login/")
def hotel_bookingPdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    logo = ImageReader('https://i.ibb.co/MPcBtHf/logo1.jpg')

    name = reservationnew.user_name
    mail = reservationnew.user_email
    phone = reservationnew.user_phone
    checkin = reservationnew.checkin_date
    checkout = reservationnew.checkout_date
    hotel_name = reservationnew.hotel_name
    room_number = reservationnew.room_numbers
    room_type = reservationnew.room_type

    hotel_reservation_instance = HotelReservation.objects.create(user_name=name, user_email=mail, user_phone=phone,
                                                                 checkin_date=checkin, checkout_date=checkout,
                                                                 hotel_name=hotel_name, room_number=room_number,
                                                                 room_type=room_type, user=request.user)
    hotel_reservation_instance.save()

    lines = [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",

        "                                     Welcome to Bon Voyage",
        " ",
        "                           Your Reservation confirmation is below",
        " ",
        " ",
        " ",
        "        Full name: " + name,
        " ",
        "        Email: " + mail,
        " ",
        "        Phone: " + phone,
        " ",
        "        Check-in date: " + checkin,
        " ",
        "        Check-out date: " + checkout,
        " ",
        "        Hotel name: " + hotel_name,
        " ",
        "        Total number of rooms: " + room_number,
        " ",
        "        Room type: " + room_type,
        " ",
        " ",
        "",
        "                               Thank you for visiting Bon Voyage",
        "",
        "                              All right reserved by Bon Voyage team",

    ]

    for line in lines:
        textob.textLine(line)

    c.drawImage(logo, 170, 10, mask='auto', anchor='c')
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='room.pdf')

@login_required(login_url="/account/login/")
def reservationnew(request):
    reservationnew.user_name = request.POST.get('user-name')
    reservationnew.user_email = request.POST.get('user-email')
    reservationnew.user_phone = request.POST.get('user-phone')
    reservationnew.checkin_date = request.POST.get('checkin-date')
    reservationnew.checkout_date = request.POST.get('checkout-date')
    reservationnew.hotel_name = request.POST.get('hotel-name')
    reservationnew.room_numbers = request.POST.get('room-numbers')
    reservationnew.room_type = request.POST.get('room-type')

    return render(request, 'main/reservationnew.html',
                  {'user_name': reservationnew.user_name, 'user_email': reservationnew.user_email,
                   'user_phone': reservationnew.user_phone, 'checkin_date': reservationnew.checkin_date,
                   'checkout_date': reservationnew.checkout_date, 'hotel_name': reservationnew.hotel_name,
                   'room_numbers': reservationnew.room_numbers, 'room_type': reservationnew.room_type})