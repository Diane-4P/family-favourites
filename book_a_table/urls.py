""" Imports from django and book_a_table views """
from django.urls import path
from . import views

# URL patterns for book_a_table app
urlpatterns = [
    path('', views.book_a_table, name='book_a_table'),
    path('bookings/', views.bookings, name='bookings'),
    path('edit_bookings/<int:booking_id>/', views.edit_bookings, name='edit_bookings'),
    path('delete_bookings/<int:booking_id>/', views.delete_bookings, name='delete_bookings'),
]