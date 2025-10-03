""" Imports from django and book_a_table views """
from django.urls import path
from . import views

# URL patterns for book_a_table app
urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book_a_table/', views.book_a_table, name='book_a_table'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]