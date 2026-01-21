""" Imports from django and other modules """
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phonenumber = PhoneNumberField(unique=True, null=False, blank=False, max_length=13, default='+441234567890')    
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'You will be contacted via {self.email} or {self.phonenumber} relating to your query as soon as possible.'
