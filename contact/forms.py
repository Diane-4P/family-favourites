"""
Imports from django and Contact models and forms
"""
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """ Form for contacting Family Favourites """
    
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phonenumber', 'message']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phonenumber': 'Telephone Number',           
        }
        widgets = {
            'phonenumber': forms.NumberInput(attrs={'max': 11}),
            'message': forms.Textarea(attrs={'rows': 4}),                 
        }
