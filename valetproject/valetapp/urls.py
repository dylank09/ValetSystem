from django.urls import path
from .views import views
from .views import auth
from .views import booking
from .views import exportToCSV

urlpatterns = [
    path('', auth.register, name='index'),
    path('bookingservice_form/', booking.bookingCreate, name='BookingView'),
    path('payForBooking/<int:bookingId>',
         booking.payForBooking, name='payForBooking'),
    path('cancel_list/', booking.viewUserBookings, name='viewUsersBookings'),
    path('cancelBooking/<int:bookingID>',
         booking.cancelBooking, name='cancelBooking'),
    path('register/', auth.register, name='register'),
    path('home/', views.home, name='home'),
    path('view/', exportToCSV.getVisitor, name='getVisitor'),
    path('login/', auth.loginPage, name='loginUser'),
]
