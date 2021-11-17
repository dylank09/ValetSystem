from django.urls import path
from .views import views
from .views import auth
from .views import booking
from .views.booking import BookingList
from .views import exportToCSV

urlpatterns = [
    path('', auth.register, name='index'),
    path('bookingservice_form/', booking.bookingCreate, name='BookingView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('payForBooking/<int:bookingId>',
         booking.payForBooking, name='payForBooking'),
    path('register/', auth.register, name='register'),
    path('home/', views.home, name='home'),
    path('view/', exportToCSV.getVisitor, name='getVisitor'),
    path('login/', auth.loginPage, name='loginUser'),
]
