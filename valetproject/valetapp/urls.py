from django.urls import path
from .views import views
from .views.views import BookingList

urlpatterns = [
     path('', views.index, name='index'),
     path('bookingservice_form/', views.bookingCreate, name='BookingView'),
     path('booking_list/', BookingList.as_view(), name='BookingList'),
     path('chainstore/<int:chainstore_id>',
          views.chainstore_by_id, name='chainstore_by_id'),
     path('booking/<int:bookingId>',
          views.viewBooking, name='viewBooking'),
     path('payForBooking/<int:bookingId>',
          views.payForBooking, name='payForBooking'),    
     path('register/', views.register, name='register'),
     path('home/', views.home, name='home'),
     path('selecttime/', views.selecttime, name='selecttime'),
     path('login/', views.loginPage, name='loginUser')
]
