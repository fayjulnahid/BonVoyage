from django.contrib import admin

# Register your models here.
from .models import userProfile, RoomModel, HotelReview, HotelReservation, chat, Contact,chatForumMessages

admin.site.register(userProfile)
admin.site.register(RoomModel)
admin.site.register(HotelReview)
admin.site.register(HotelReservation)
admin.site.register(chat)
admin.site.register(chatForumMessages)
admin.site.register(Contact)