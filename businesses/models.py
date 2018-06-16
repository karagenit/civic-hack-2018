from django.db import models
from accounts.models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)

    @receiver(post_save, sender=Profile)
    def create_user_business(sender, instance, created, **kwargs):
        if created:
            Business.objects.create(profile=instance)

    @receiver(post_save, sender=Profile)
    def save_user_business(sender, instance, **kwargs):
        #TODO: should be able to delete all the except: stuff after all the users have run this
        if instance.member_type == '3':
            instance.business.save()



class PickupRequest(models.Model):
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    date_created = models.DateField()
    available_for = models.DurationField()

class FoodItem(object):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
    )
    number = models.IntegerField(default=0)
    
