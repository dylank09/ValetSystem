from django.shortcuts import render
from django.http import request

import pytz

utc = pytz.UTC

def index():
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')
    