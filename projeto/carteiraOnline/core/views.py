from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')