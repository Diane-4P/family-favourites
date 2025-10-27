""" Imports from django and other modules """
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class BookATable(models.Model):
    """ Model to represent a table booking """
    
    TIME_CHOICES = (
        (0, '12:00 PM'),
        (1, '12:15 PM'),
        (2, '12:30 PM'),
        (3, '12:45 PM'),
        (4, '1:00 PM'),
        (5, '1:15 PM'),
        (6, '1:30 PM'),
        (7, '1:45 PM'),
        (8, '2:00 PM'),
        (9, '2:15 PM'),
        (10, '2:30 PM'),
        (11, '2:45 PM'),
        (12, '3:00 PM'),
        (13, '3:15 PM'),
        (14, '3:30 PM'),
        (15, '3:45 PM'),
        (16, '4:00 PM'),
        (17, '4:15 PM'),
        (18, '4:30 PM'),
        (19, '4:45 PM'),
        (20, '5:00 PM'),
        (21, '5:15 PM'),
        (22, '5:30 PM'),
        (23, '5:45 PM'),
        (24, '6:00 PM'),
        (25, '6:15 PM'),
        (26, '6:30 PM'),
        (27, '6:45 PM'),
        (28, '7:00 PM'),
        (29, '7:15 PM'),
        (30, '7:30 PM'),
        (31, '7:45 PM'),
        (32, '8:00 PM'),
        (33, '8:15 PM'),
        (34, '8:30 PM'),
        (35, '8:45 PM'),
        (36, '9:00 PM'),
    )
    
    OCCASIONS = (
        (0, 'None'),
        (1, 'Birthday'),
        (2, 'Anniversary'),
        (3, 'Business Meal'),
        (4, 'Family Meal'),
        (5, 'Date Night'),     
        (6, 'Other'),
    )
    
    APPROVED = (
        (0, "Awaiting Booking Confirmation"),
        (1, "Booking Confirmed"),
    )
    
    def validate_date(self):
        """
        Display error message, if the date selected is in the past.
        """
        if self < date.today():
            raise ValidationError("Date cannot be in the past.")
        
    date = models.DateField(
        validators=[validate_date]
    )
       
    book_table_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    time = models.IntegerField(choices=TIME_CHOICES, default=0)
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    occasion = models.IntegerField(choices=OCCASIONS, default=0)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phonenumber = PhoneNumberField(unique=True, null=False, blank=False, max_length=13, default='+441234567890')
    approved = models.IntegerField(choices=APPROVED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
     
    class Meta:
                ordering = ["-created_on"]
    
    def clean(self):
        # Ensure booking date is not in the past
        if self.booking_date <= date.today():
            raise ValidationError('Booking date cannot be in the past.')

        # Ensure number of guests is at least 1
        if self.number_of_guests <= 1:
            raise ValidationError('Number of guests must be at least 1.')
            
    def __str__(self):
        return f'Booking for {self.user.username} on {self.date} at {self.get_time_display()} for {self.number_of_guests} guests. Occasion: {self.get_occasion_display()}. Special Requests: {self.special_requests if self.special_requests else "None"}. You will be contacted via {self.email} or {self.phonenumber} of confirmation of booking.'

    @property
    def past_date(self):
        """
        Decorator to check if date is in the past.
        """
        today = date.today()
        if self.date < today:
            return True