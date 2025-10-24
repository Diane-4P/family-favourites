from django.shortcuts import render
from .models import Menu

# Create your views here.
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu' : menu_data})