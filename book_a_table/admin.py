"""Imports from django and BookATable models"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import BookATable


# Register your models here.
@admin.register(BookATable)
class BookATableAdmin(ModelAdmin):
    """ Admin view for BookATable model """
    
    list_display = ('book_table_id', 'user', 'first_name', 'last_name', 'email', 'phonenumber', 'booking_date', 'booking_time', 'number_of_guests', 'special_requests', 'occasion', 'created_on', 'approved')
    ordering = ('-booking_date', '-booking_time')
    search_fields = ('user__username', 'booking_date')
    list_filter = ('booking_date', 'booking_time')