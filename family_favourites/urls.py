"""
URL configuration for family_favourites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('menu/', include('menu.urls')),
    path('book_a_table/', include('book_a_table.urls')),
    path('accounts/', include('allauth.urls'))
]
