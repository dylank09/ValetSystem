from django.contrib import admin

from .models.ChainStore import ChainStore
from .models.users.customer import Customer
# admin.site.register(Customer)
admin.site.register(ChainStore)
