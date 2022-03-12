from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .models import Conta

# Create your views here.

def home(request, user_id):
    data = Conta.objects.get(nr_conta_text=user_id)
    return render(request, 'core/home.html', {'obj': data})

def login(request):
    return render(request, 'core/login.html')