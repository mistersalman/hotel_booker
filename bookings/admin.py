from django.contrib import admin

# Register your models here.
from .models import HotelSetting, Reservation
admin.site.register(HotelSetting)
admin.site.register(Reservation)