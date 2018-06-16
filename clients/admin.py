from django.contrib import admin
from .models import Client, PickupRequest, BusinessRequest

admin.site.register(Client)
admin.site.register(PickupRequest)
admin.site.register(BusinessRequest)
