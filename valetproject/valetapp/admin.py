from django.contrib import admin

from .models.chainstore import ChainStore
from .models.users.customer import Customer
from .models.users.staff import Staff
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(ChainStore)
