from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

class PickupRequest(models.Model):
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    date_created = models.DateField()
    available_for = models.DurationField()
