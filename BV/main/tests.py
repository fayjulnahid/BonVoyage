from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
#from main.forms import HotelReview, ResturantReview, PlaceReview

#from main.models import RoomModel, Place, ResturantInfo

from main.views import index, UserProfile, createProfile, about, RoomShow, hotel_page, \
    hotelReview, deleteHotelReview, hotel_bookingPdf, reservationnew, hotelsearch, \
    directmessage, sentmessage,contact

from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class UrlsTest(SimpleTestCase):

    def test_index(self):
        url = reverse('main:base_template')
        self.assertEquals(resolve(url).func, index)

    def test_UserProfile(self):
        url = reverse('main:user_profile')
        self.assertEquals(resolve(url).func, UserProfile)

    def test_createProfile(self):
        url = reverse('main:create_profile')
        self.assertEquals(resolve(url).func, createProfile)

    def test_about(self):
        url = reverse('main:about')
        self.assertEquals(resolve(url).func, about)

    def test_contact(self):
        url = reverse('main:contact')
        self.assertEquals(resolve(url).func, contact)

    def test_hotelReview(self):
        url = reverse('main:hotelReview')
        self.assertEquals(resolve(url).func, hotelReview)

    def test_hotel_bookingPdf(self):
        url = reverse('main:hotel_bookingPdf')
        self.assertEquals(resolve(url).func, hotel_bookingPdf)

    def test_RoomShow(self):
        url = reverse('main:hotel_page')
        self.assertEquals(resolve(url).func, hotel_page)

    def test_hotel_page(self):
        url = reverse('main:RoomShow')
        self.assertEquals(resolve(url).func, RoomShow)

    def test_reservationnew(self):
        url = reverse('main:reservation_new')
        self.assertEquals(resolve(url).func, reservationnew)

    def test_directmessage(self):
        url = reverse('main:direct_message')
        self.assertEquals(resolve(url).func, directmessage)

    def test_sentmessage(self):
        url = reverse('main:sent_message')
        self.assertEquals(resolve(url).func, sentmessage)

class ViewTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('main:base_template'))
        self.assertEquals(response.status_code, 200)
    def test_about(self):
        response = self.client.get(reverse('main:about'))
        self.assertEquals(response.status_code, 200)

