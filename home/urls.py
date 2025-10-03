""" Imports from django and home views """
from django.urls import path
from . import views

# URL patterns for book_a_table app
urlpatterns = [
    path('', views.index, name='index')
]