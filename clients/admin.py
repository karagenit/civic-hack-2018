from django.contrib import admin
from .models import Client, PickupRequest

admin.site.register(Client)
admin.site.register(PickupRequest)
