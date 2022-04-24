from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='base_template'),

    url(r'^user_profile/$', views.UserProfile, name="user_profile"),
    url(r'^create_profile/$', views.createProfile, name="create_profile"),
    path('about/', views.about, name='about'),

    url(r'^hotel_page/$', views.hotel_page, name="hotel_page"),
    path('room/', views.RoomShow, name="RoomShow"),

    url(r'^reservation_new/$', views.reservationnew, name="reservation_new"),
    path('hotel_bookingPdf', views.hotel_bookingPdf, name="hotel_bookingPdf"),

    url(r'^hotelReview/$', views.hotelReview, name="hotelReview"),
    url(r'^hotelsearch/$', views.hotelsearch, name="hotelsearch"),
    #path('deleteHotelReview/<str:pk>/$', views.deleteHotelReview, name="deleteHotelReview"),

    url(r'^direct_message/$', views.directmessage, name="direct_message"),
    url(r'^sent_message/$', views.sentmessage, name="sent_message"),

    url(r'^chat_forum/$', views.chatForum, name="chat_forum"),

    path('contact/',views.contact, name='contact'),


]