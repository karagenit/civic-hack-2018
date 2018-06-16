from django.db import models
from accounts.models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from businesses.models import FoodItem

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(FoodItem, related_name="cart")

    objects = models.Manager()

    # TODO some way to ask for/schedule 'drop-offs'
    @receiver(post_save, sender=Profile)
    def create_user_client(sender, instance, **kwargs):
        if instance.member_type == '1':
            Client.objects.create(profile=instance)

    @receiver(post_save, sender=Profile)
    def save_user_client(sender, instance, **kwargs):
        #TODO: should be able to delete all the except: stuff after all the users have run this
        if instance.member_type == '1':
            instance.client.save()

class PickupRequest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(FoodItem, related_name="request_fooditems")
    date_created = models.DateTimeField()

    
