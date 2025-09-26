""" Imports from django, book_a_table models and forms """
from django.shortcuts import render
from django.contrib import messages
from .models import BookATable, BookingDetails
from .forms import BookATableForm, BookingDetailsForm


# Create your views here.
def add_book_a_table(request):
    """ View to handle table booking form """
    
    if request.method == 'POST':
        if request.user.is_superuser or not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to book a table.')
            return render(request, 'book_a_table/book_a_table.html', {'form': BookATableForm()})
        form = BookATableFormAdmin(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.validate_date()
                booking.save()
                messages.success(request, 'Table booked successfully!')
            except ValidationError as e:
                form.add_error('booking_date', e.message)
        else:        
            form = BookATableForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                try:
                    booking.validate_date()
                    booking.save()
                    messages.success(request, 'Table booked successfully!')
                except ValidationError as e:
                    form.add_error('booking_date', e.message)
    else:
        if request.user.is_superuser:
            form = BookATableFormAdmin()
        else:
            form = BookATableForm()
    
    return render(request, 'book_a_table/book_a_table.html', {'form': form})

