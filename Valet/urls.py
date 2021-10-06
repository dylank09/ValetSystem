from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poopy', views.poopy, name='poopy'),
]
