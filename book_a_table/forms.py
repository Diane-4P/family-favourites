"""
Imports from django and book_a_table and booking_details models and forms
"""
from django import forms
from .models import BookATable, BookingDetails

class BookATableForm(forms.ModelForm):
    """ Form for booking a table """
    
    class Meta:
        model = BookATable
        fields = ['booking_date', 'booking_time', 'number_of_guests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
        }
        
class BookATableFormAdmin(forms.ModelForm):
    """ Form for admin to book a table for any user """
    
    class Meta:
        model = BookATable
        fields = ['user', 'first_name', 'last_name', 'email', 'phone_number', 'special_requests', 'occasion''booking_date', 'booking_time', 'number_of_guests']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'special_requests': 'Special Requests (optional)',
            'occasion': 'Occasion (optional)',
        }
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
        }
        
class BookingDetailsForm(forms.ModelForm):
    """ Form for adding additional booking details """
    
    class Meta:
        model = BookingDetails
        fields = ['user', 'first_name', 'last_name', 'email', 'phone_number', 'special_requests', 'occasion']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'special_requests': 'Special Requests (optional)',
            'occasion': 'Occasion (optional)',
        }
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 4}),
            'occasion': forms.Select(),
        }
        