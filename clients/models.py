from django.db import models

# Create your models here.

class Client(models.model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    # TODO some way to ask for/schedule 'drop-offs'
