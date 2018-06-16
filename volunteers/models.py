from django.db import models
from accounts.models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length=128)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    objects = models.Manager()
    last_location = models.CharField(max_length=1028, default='Union 525, Indianapolis, IN')


    @receiver(post_save, sender=Profile)
    def create_user_volunteer(sender, instance, created, **kwargs):
        if instance.member_type == '2':
            Volunteer.objects.create(profile=instance)

    @receiver(post_save, sender=Profile)
    def save_user_volunteer(sender, instance, **kwargs):
        #TODO: should be able to delete all the except: stuff after all the users have run this
        if instance.member_type == '2':
            instance.volunteer.save()
