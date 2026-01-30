""" Imports from django, book_a_table models and forms """
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BookATable
from .forms import BookATableForm, BookATableFormAdmin


# Create your views here.
@login_required
def bookings(request):
    """ 
    View to display all bookings - admin only
    Other users will only see their own bookings
    Both views are ordered by date and time in descending order 
    """
    
    if request.user.is_superuser:
        bookings = BookATable.objects.all().order_by('-date', '-time')
    else:
        bookings = BookATable.objects.filter(user=request.user).order_by('-date', '-time')
    context = {
            'bookings': bookings,
        }
    
    return render(request, 'book_a_table/bookings.html', context)
    

@login_required
def book_a_table(request):
    """ View to handle table booking form """
    
    if request.method == 'POST':
        if request.user.is_superuser:
            form = BookATableFormAdmin(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                try:
                    booking.full_clean()
                    booking.save()
                    messages.success(request, 'Table booked successfully!')
                except ValidationError as e:
                    form.add_error('date', e.message)
                return redirect('bookings')
            else:
                messages.error(request, 'Request unsuccessful!')
                return render(request, 'book_a_table/book_a_table.html', {'form': form})
        else:        
            form = BookATableForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                try:
                    booking.full_clean()
                    booking.save()
                    messages.success(request, 'Table booked successfully! Pending confirmation from Family Favourites.')
                except ValidationError as e:
                    form.add_error('date', e.message)
                return redirect('bookings')
            else:
                messages.error(request, 'Request unsuccessful!')
                return render(request, 'book_a_table/book_a_table.html', {'form': form})
    else:
        if request.user.is_superuser:
            form = BookATableFormAdmin()
        else:
            form = BookATableForm()
    
    return render(request, 'book_a_table/book_a_table.html', {'form': form})


@login_required
def edit_bookings(request, booking_id):
    """ 
    View to handle editing a booking - admin only 
    Other users can edit their own bookings via a different view
    """
    
    booking = get_object_or_404(BookATable, pk=booking_id)
        
    if request.user.is_superuser:
        formClass = BookATableFormAdmin
    else:
        formClass = BookATableForm
        
    if request.method == 'POST':
        form = formClass(request.POST, instance=booking)
        if form.is_valid():
            edited_booking = form.save(commit=False)
            try:
                edited_booking.full_clean()
                edited_booking.save()
                messages.success(request, 'Booking updated successfully!')
                return redirect('bookings')
            except ValidationError as e:
                form.add_error('date', e.message)
    else:
        form = formClass(instance=booking)
    
    return render(request, 'book_a_table/edit_bookings.html', {'form': form, 'booking': booking})


@login_required
def delete_bookings(request, booking_id):
    """ 
    View to handle deleting a booking - admin only 
    Other users can delete their own bookings via a different view
    """
    
    booking = get_object_or_404(BookATable, pk=booking_id)
    if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to delete a booking.')
            return redirect('login')
    if not request.user.is_superuser and booking.user != request.user:
            messages.error(request, 'You do not have permission to delete this booking.')
            return redirect('bookings')      
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('bookings')
            
    return render(request, 'book_a_table/delete_bookings.html', {'booking': booking})
