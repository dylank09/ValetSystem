from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse, request
from valetapp.views.concreteVisitor import ConcreteVisitor

from valetapp.views.visitor import Visitor
from .concreteVisitor import ConcreteVisitor

import pytz
from django.contrib.auth import login

utc = pytz.UTC

def index():
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')
