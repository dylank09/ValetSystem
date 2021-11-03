import datetime
from valetapp.models import Booking

def check_availability(start_time, end_time):
    avail_list=[]
    booking_list = Booking.objects.filter(start_time = start_time)
    for booking in booking_list:
        if booking.start_time > end_time or booking.end_time < start_time:
            avail_list.append[True]
        else:
            avail_list.append[False]
    return all(avail_list)