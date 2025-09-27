""" Imports from django, book_a_table models and forms """
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import BookATable
from .forms import BookATableForm, BookingDetailsForm


# Create your views here.
def bookings(request):
    """ 
    View to display all bookings - admin only
    Other users will only see their own bookings
    Both views are ordered by date and time in descending order 
    """
    
    if request.user.is_superuser:
        messages.error(request, 'Only admin users can view all bookings.')
            
        bookings = BookATable.objects.all().order_by('-booking_date', '-booking_time')
        context = {
            'bookings': bookings,
        }
    else:
        user_filter = BookATable.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
        
    return render(request, 'book_a_table/bookings.html', context)
    

def book_a_table(request):
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


def booking_details(request, booking_id):
    """ View to handle booking details form """
    
    try:
        booking = BookATable.objects.get(book_table_id=booking_id)
    except BookATable.DoesNotExist:
        messages.error(request, 'Booking does not exist.')
        return render(request, 'book_a_table/bookings.html', {})
    
    if request.method == 'POST':
        form = BookingDetailsForm(request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.book_a_table = booking
            details.save()
            messages.success(request, 'Booking details added successfully!')
            return redirect('bookings')
    else:
        form = BookingDetailsForm()
    
    return render(request, 'book_a_table/booking_details.html', {'form': form, 'booking': booking})


def edit_booking(request, booking_id):
    """ 
    View to handle editing a booking - admin only 
    Other users can edit their own bookings via a different view
    """
    
    if request.user.is_superuser:
        messages.error(request, 'Only admin users can edit bookings.')
    
    try:
        booking = BookATable.objects.get(book_table_id=booking_id)
    except BookATable.DoesNotExist:
        messages.error(request, 'Booking does not exist.')
        return render(request, 'book_a_table/bookings.html', {})
    
    if request.method == 'POST':
        if request.user.is_superuser:
            form = BookATableFormAdmin(request.POST, instance=booking)
        if form.is_valid():
            edited_booking = form.save(commit=False)
            try:
                edited_booking.validate_date()
                edited_booking.save()
                messages.success(request, 'Booking updated successfully!')
                return redirect('bookings')
            except ValidationError as e:
                form.add_error('booking_date', e.message)
    else:
        form = BookATableFormAdmin(instance=booking)
    
    return render(request, 'book_a_table/edit_booking.html', {'form': form, 'booking': booking})


def delete_booking(request, booking_id):
    """ 
    View to handle deleting a booking - admin only 
    Other users can delete their own bookings via a different view
    """
    
    booking = get_object_or_404(BookATable, pk=booking_id)
    if request.user.is_superuser:
        messages.error(request, 'Only admin users can delete bookings.')
    
    try:
        booking = BookATable.objects.get(book_table_id=booking_id)
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('bookings')
    except BookATable.DoesNotExist:
        messages.error(request, 'Booking does not exist.')
        
    else:
        user_filter = BookATable.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
    
    return render(request, 'book_a_table/bookings.html', {})

    