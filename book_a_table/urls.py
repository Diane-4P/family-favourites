""" Imports from django and book_a_table views """
from django.urls import path
from . import views

# URL patterns for book_a_table app
urlpatterns = [
    path('bookings', views.bookings, name='bookings'),
    path('book_a_table/', views.book_a_table, name='book_a_table'),
    path('edit/<int:book_table_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:book_table_id>/', views.delete_booking, name='delete_booking'),
]