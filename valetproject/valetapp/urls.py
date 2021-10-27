from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chainstore/<int:chainstore_id>', views.chainstore_by_id, name='chainstore_by_id'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('bookingscreen/', views.bookingscreen, name= 'bookingscreen')
=======
    path('home/', views.home, name='home'),
>>>>>>> 9b4eedd73754c8d637bad2d2534901685564f1fa
]