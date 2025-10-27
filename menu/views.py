from django.shortcuts import render, get_object_or_404
from .models import Menu

# Create your views here.
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu/menu.html', {'menu' : menu_data})