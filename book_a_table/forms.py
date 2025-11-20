"""
Imports from django and BookATable models and forms
"""
from django import forms
from .models import BookATable

class BookATableForm(forms.ModelForm):
    """ Form for booking a table """
    
    class Meta:
        model = BookATable
        fields = ['date', 'time', 'number_of_guests', 'first_name', 'last_name', 'email', 'phonenumber', 'occasion', 'special_requests']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phonenumber': 'Telephone Number',
            'occasion': 'Occasion (optional)',
            'special_requests': 'Special Requests (optional)',            
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'phonenumber': forms.NumberInput(attrs={'max': 11}),
            'occasion': forms.Select(),
            'special_requests': forms.Textarea(attrs={'rows': 4}),            
        }
        
class BookATableFormAdmin(forms.ModelForm):
    """ Form for admin to book a table for any user """
    
    class Meta:
        model = BookATable
        fields = ['date', 'time', 'number_of_guests', 'user', 'first_name', 'last_name', 'email', 'phonenumber', 'occasion', 'special_requests','approved']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phonenumber': 'Telephone Number',
            'occasion': 'Occasion (optional)',
            'special_requests': 'Special Requests (optional)',            
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'number_of_guests': forms.NumberInput(attrs={'min': 1}),
            'phonenumber': forms.NumberInput(attrs={'max': 11}),
            'occasion': forms.Select(),
            'special_requests': forms.Textarea(attrs={'rows': 4}),            
        }
        