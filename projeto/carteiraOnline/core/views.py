from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .conversao import conversao
from .models import Conta
import re

# Create your views here.

def home(request, user_id):
    data = Conta.objects.get(nr_conta_text=user_id)
    euro = data.money_text
    dollar = conversao(euro,"dollar")
    return render(request, 'core/home.html', {'obj': data, 'money': {"euro": '{:,}'.format(euro), "dollar": dollar}})

def extrato(request, user_id):
    data = Conta.objects.get(nr_conta_text=user_id)
    trans = []
    ext = data.pub_date.split(";")
    ext.remove('')
    for e in ext:
        print(e)
        name = e.split("---")[0]
        value = re.search(r'\((.*?)\)',e).group(1)
        day = re.search(r'\[(.*?)\]',e).group(1)
        trans.append({
            'name': name,
            'value': value,
            'day': day
        })
    return render(request, 'core/extrato.html', {'data': trans})

def login(request):
    return render(request, 'core/login.html')