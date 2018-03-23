from django.db import models

# Create your models here.


class HotelSetting(models.Model):
    max_rooms = models.IntegerField()
    max_overbook = models.IntegerField()
    day = models.DateField()


class Reservation(models.Model):
    day = models.ForeignKey(HotelSetting, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

