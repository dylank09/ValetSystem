from django.contrib import admin

from .models import ChainStore
from .models.users import Customer
admin.site.register(Customer)
admin.site.register(ChainStore)
