"""
Imports from django and BookATable models and forms
"""
from django import forms
from .models import BookATable

class BookATableForm(forms.ModelForm):
    """ Form for booking a table """
    
    class Meta:
        model = BookATable
        fields = ['booking_date', 'booking_time', 'number_of_guests', 'first_name', 'last_name', 'email', 'phonenumber', 'special_requests', 'occasion']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phonenumber': 'Telephone Number',
            'special_requests': 'Special Requests (optional)',
            'occasion': 'Occasion (optional)',
        }
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
            'phonenumber': forms.NumberInput(attrs={'max': 11}),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
            'occasion': forms.Select(),
        }
        
class BookATableFormAdmin(forms.ModelForm):
    """ Form for admin to book a table for any user """
    
    class Meta:
        model = BookATable
        fields = ['booking_date', 'booking_time', 'number_of_guests', 'user', 'first_name', 'last_name', 'email', 'phonenumber', 'special_requests', 'occasion']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phonenumber': 'Telephone Number',
            'special_requests': 'Special Requests (optional)',
            'occasion': 'Occasion (optional)',
        }
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
            'phonenumber': forms.NumberInput(attrs={'max': 11}),
            'special_requests': forms.Textarea(attrs={'rows': 4}),
            'occasion': forms.Select(),
        }
        