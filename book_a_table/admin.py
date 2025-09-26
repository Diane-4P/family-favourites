from django.contrib import admin
from .models import BookATable, BookingDetails

# Register your models here.
admin.site.register(BookATable)
admin.site.register(BookingDetails)