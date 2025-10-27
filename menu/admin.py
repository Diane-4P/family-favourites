"""Imports from django and Menu models"""
from django.contrib import admin
from .models import Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """ Admin view for Menu model """
    
    list_display = ('main_title', 'sub_menu_title', 'item_name', 'price', 'description')
    search_fields = ('item_name',)
    list_filter = ('main_title', 'sub_menu_title',)
    