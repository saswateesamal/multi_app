from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(request):
    return HttpResponse('<h1>Rohit is the captain of MI</h1>')
