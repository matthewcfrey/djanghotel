from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    num_beds = models.IntegerField()
    smoking = models.BooleanField()
    description = models.CharField(max_length = 500)
    def __int__(self):
        return self.room_number
    
class RoomCost(models.Model):
    room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.CASCADE)
    cost = models.FloatField()

    def __int__(self):
        return self.room_number
    

class DjanghotelUser(models.Model):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length = 500)
    last_name = models.CharField(max_length = 500)

    def __str__(self):
        return self.email

class Booking(models.Model):
    email = models.ForeignKey(DjanghotelUser, blank=True, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, blank=True, null=True, on_delete=models.CASCADE)


