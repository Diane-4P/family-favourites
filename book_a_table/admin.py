"""Imports from django and book_a_table models"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import BookATable, BookingDetails


# Register your models here.
admin.site.register(BookATable)
admin.site.register(BookingDetails)


@admin.register(BookATable)
class BookATableAdmin(ModelAdmin):
    """ Admin view for BookATable model """
    
    list_display = ('book_table_id', 'user', 'first_name', 'last_name', 'email', 'phone_number', 'booking_date', 'booking_time', 'number_of_guests' 'special_requests', 'occasion')
    ordering = ('-booking_date', '-booking_time')
    search_fields = ('user__username', 'booking_date')
    list_filter = ('booking_date', 'booking_time')