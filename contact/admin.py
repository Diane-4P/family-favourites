"""Imports from django and BookATable models"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    """ Admin view for Contact model """
    
    list_display = ('contact_id', 'first_name', 'last_name', 'email', 'phonenumber', 'message')
    search_fields = ('user__last_name', 'first_name')
    