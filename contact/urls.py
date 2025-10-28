""" Imports from django and contact views """
from django.urls import path
from . import views

# URL patterns for contact app
urlpatterns = [
    path('', views.contact, name='contact'),
]