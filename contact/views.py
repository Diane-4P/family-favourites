from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm


# Create your views here.
def contact(request):
    """ View to handle contact form """
    
    if request.method == 'POST':      
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            try:
                contact.full_clean()
                contact.save()
                messages.success(request, 'Message sent successfully! Awaiting message from Family Favourites.')
                return redirect('index')
            except:
                messages.error(request, 'Message failed!')
                
            
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})


@login_required
def contacts(request):
    """ View to display all contacts - admin only """
    
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Admins only.')
        return redirect('index')
    
    contacts = Contact.objects.all()    
        
    context = {
            'contacts': contacts,
        }
    
    return render(request, 'contact/contacts.html', context)


