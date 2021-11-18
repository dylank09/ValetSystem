from django.urls import path
from .views import views
from .views import auth
from .views import booking
from .views import exportToCSV
from .views.booking import BookingList

urlpatterns = [
    path('', auth.register, name='index'),
    path('bookingservice_form/', booking.init_booking_form, name='BookingView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('payForBooking/<int:bookingId>',
         booking.pay_for_booking, name='payForBooking'),
    path('cancel_list/', booking.viewUserBookings, name='viewUsersBookings'),
    path('cancelBooking/<int:bookingID>', booking.cancel_booking, name='cancelBooking'),
    path('register/', auth.register, name='register'),
    path('home/', views.home, name='home'),
    path('view/', exportToCSV.getVisitor, name='getVisitor'),
    path('login/', auth.login_page, name='loginUser'),
]
