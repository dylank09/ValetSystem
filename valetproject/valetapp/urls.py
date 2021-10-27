from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chainstore/<int:chainstore_id>', views.chainstore_by_id, name='chainstore_by_id'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('homescreen/', views.homescreen, name='homescreen')
=======
    path('bookingscreen/', views.bookingscreen, name= 'bookingscreen'),
    path('home/', views.home, name='home'),
>>>>>>> 7ec27bf4e2a6971719533d0d04527e19d82a40f1
]