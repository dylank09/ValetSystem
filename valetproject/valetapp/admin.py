from django.contrib import admin

from .models.chainstore import ChainStore
from .models.users.customer import Customer
from .models.users.staff import Staff
from .models.booking import Booking
from .models.valet import Valet
from .models.users.membershiptype import MembershipType
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(ChainStore)
admin.site.register(Booking)
admin.site.register(Valet)
admin.site.register(MembershipType)
