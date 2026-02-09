"""Imports from django and BookATable models"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import BookATable


# Register your models here.
@admin.register(BookATable)
class BookATableAdmin(ModelAdmin):
    """ Admin view for BookATable model """

    list_display = (
        'book_table_id', 'user', 'date', 'time', 'number_of_guests',
        'special_requests', 'occasion', 'approved')
    ordering = ('-book_table_id', '-date', '-time')
    search_fields = ('user__username', 'date')
    list_filter = ('date', 'approved')
    actions = ['booking_confirmed']

    def booking_confirmed(self, request, queryset):
        queryset.update(approved=1)
