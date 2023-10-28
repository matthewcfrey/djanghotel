from django.shortcuts import render
from .models import Room, RoomCost, DjanghotelUser, Booking 

# Create your views here.

def index(request):
    rooms = RoomCost.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(request, "index.html", context)