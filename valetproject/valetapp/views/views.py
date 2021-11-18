from django.shortcuts import render, redirect
from django.http import HttpResponse, request

import pytz
from django.contrib.auth import login

utc = pytz.UTC

def index():
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')
