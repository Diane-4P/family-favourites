from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def book_a_table(request):
    return HttpResponse('Book a table page coming soon!')
