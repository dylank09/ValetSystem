from django.urls import path
from . import views
from .views import BookingList

urlpatterns = [
    path('', views.index, name='index'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('chainstore/<int:chainstore_id>',
         views.chainstore_by_id, name='chainstore_by_id'),
    path('register/', views.register, name='register'),
    path('bookingscreen/', views.bookingscreen, name='bookingscreen'),
    path('home/', views.home, name='home'),
    path('selecttime/', views.selecttime, name='selecttime'),
    path('login/', views.loginUser, name='loginUser')
]
