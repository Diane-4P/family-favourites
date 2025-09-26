""" Imports from django and other modules """
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


""" Model to represent a table booking """
class BookATable(models.Model):
    
    TIME_CHOICES = (
        ('0', '12:00 PM'),
        ('1', '12:15 PM'),
        ('2', '12:30 PM'),
        ('3', '12:45 PM'),
        ('4', '1:00 PM'),
        ('5', '1:15 PM'),
        ('6', '1:30 PM'),
        ('7', '1:45 PM'),
        ('8', '2:00 PM'),
        ('9', '2:15 PM'),
        ('10', '2:30 PM'),
        ('11', '2:45 PM'),
        ('12', '3:00 PM'),
        ('13', '3:15 PM'),
        ('14', '3:30 PM'),
        ('15', '3:45 PM'),
        ('16', '4:00 PM'),
        ('17', '4:15 PM'),
        ('18', '4:30 PM'),
        ('19', '4:45 PM'),
        ('20', '5:00 PM'),
        ('21', '5:15 PM'),
        ('22', '5:30 PM'),
        ('23', '5:45 PM'),
        ('24', '6:00 PM'),
        ('25', '6.15 PM'),
        ('26', '6:30 PM'),
        ('27', '6:45 PM'),
        ('28', '7:00 PM'),
        ('29', '7:15 PM'),
        ('30', '7:30 PM'),
        ('31', '7:45 PM'),
        ('32', '8:00 PM'),
        ('33', '8:15 PM'),
        ('34', '8:30 PM'),
        ('35', '8:45 PM'),
        ('36', '9:00 PM'),
    )
    
    book_table_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings')
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=TIME_CHOICES, default='0')
    number_of_guests = models.PositiveIntegerField()
        
    def validate_date(self):
        """ Ensure booking date is not in the past """
        if self.booking_date < date.today():
            raise ValidationError('Booking date cannot be in the past.')

        """ Ensure number of guests is at least 1 """
        if self.number_of_guests < 1:
            raise ValidationError('Number of guests must be at least 1.')

    def __str__(self):
        return f'Booking for {self.user.username} on {self.booking_date} at {self.booking_time} for {self.number_of_guests} guests'
    
class BookingDetails(models.Model):
    
    OCCASIONS = (
        ('0', 'None'),
        ('1', 'Birthday'),
        ('2', 'Anniversary'),
        ('3', 'business_meal'),
        ('4', 'family_meal'),
        ('5', 'date_night'),     
        ('6', 'Other'),
    )
    
    book_a_table = models.ForeignKey(BookATable, on_delete=models.CASCADE, related_name='table_booking')
    booking_details_id = models.AutoField(primary_key=True)
    special_requests = models.TextField(blank=True, null=True)
    occasion = models.IntegerField(choices=OCCASIONS, default='0')
    
    def __str__(self):
        return f'Booking Details: {self.occasion if self.occasion else "No Occasion"}'
