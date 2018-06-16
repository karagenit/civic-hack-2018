from django.db import models
from accounts.models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from businesses.models import IndividualFoodItem
from volunteers.models import Volunteer

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    cart = models.ManyToManyField(IndividualFoodItem, related_name="cart")
    objects = models.Manager()

    def get_num_items_in_cart(self, item_class):
        count = 0
        for item in self.cart.all():
            if (item.item_class == item_class):
                count = count + 1

        return count


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
    driver = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE,
        null=True,
    )
    items = models.ManyToManyField(IndividualFoodItem, related_name="requestfooditems")
    date_created = models.DateTimeField()

class Record(models.Model):
    date = models.DateField()
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )
    calories = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
