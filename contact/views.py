from django.shortcuts import render, redirect
from django.contrib import messages
from allauth.account.forms import SignupForm
from .models import Contact
from .forms import ContactForm, ContactFormAdmin


# Create your views here.
def contact(request):
    """ View to handle contact form """
    
    if request.method == 'POST':
        if request.user.is_superuser:
            form = ContactFormAdmin(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            try:
                contact.full_clean()
                contact.save()
                messages.success(request, 'Message sent successfully!')
            except:
                messages.add_error(request, 'Message failed!')
        else:        
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.user = request.user
                try:
                    contact.full_clean()
                    contact.save()
                    messages.success(request, 'Message sent successfully! Awaiting message from Family Favourites.')
                except:
                    messages.add_error(request, 'Message failed!')
    else:
        if request.user.is_superuser:
            form = ContactFormAdmin()
        else:
            form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})


def contacts(request):
    """ View to display all contacts - admin only """
    
    if request.user.is_superuser:
        contacts = Contact.objects.all()
    elif not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view your contact information.')
        return redirect('login')
    else:
        contacts = Contact.objects.filter(user=request.user)
    context = {
            'contacts': contacts,
        }
    
    return render(request, 'contact/contact.html', context)


def register_signup(request):
    """ View to handle contact form """
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            register_signup = form.save(commit=False)
            register_signup.user = request.user
            try:
                register_signup.full_clean()
                register_signup.save()
                messages.success(request, 'Registration successfully! Please signin.')
                return redirect('signin') 
            except:
                messages.add_error(request, 'Registration failed!')
    else:
        form = SignupForm()
    
    return render(request, 'register/register.html', {'form': form})
