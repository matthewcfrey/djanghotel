from django.contrib import admin

# Register your models here.
from .models import Room, RoomCost, DjanghotelUser, Booking

admin.site.register(Room)
admin.site.register(RoomCost)
admin.site.register(DjanghotelUser)
admin.site.register(Booking)