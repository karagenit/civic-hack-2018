from django.db import models
from accounts.models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from volunteers.models import Volunteer
from businesses.models import Business, IndividualFoodItem


# Create your models here.

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''

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
    STATUS_CHOICES = (('1', 'Requested',), ('2', 'In Progress',), ('3', 'Delivered'))
    status = models.CharField(max_length=50, default='1')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    driver = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE,
        null=True,
    )
    date_created = models.DateTimeField()

    def get_status(self):
        if (self.status == '1' or self.status == '3'):
            return self.status
        elif (self.status == '2'):
            biz_req = self.current()
            return biz_req.status

    def all_pickups_done(self):
        bool = True
        for biz_req in self.business_set.all():
            bool = bool and (biz_req.status == '4')

        return bool

    def accept(self):
        self.status = '2'
        self.save()

    def next_business_request(self):
        return BusinessRequest.objects.filter(parentRequest=self, status='1').first()

    def current(self):
        return BusinessRequest.objects.filter(parentRequest=self, is_running=True).first()




class BusinessRequest(models.Model):
    is_running = models.BooleanField(default=False)
    STATUS_CHOICES = (('1', 'Waiting',), ('2', 'In Progress',), ('3', 'Arrived'), ('4', 'Picked Up'))
    status = models.CharField(max_length=50, default='1')
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(IndividualFoodItem, related_name="requestfooditems")
    parentRequest = models.ForeignKey(
        PickupRequest,
        on_delete=models.CASCADE,
        related_name='business_set'
    )

    def start(self):
        self.is_running = True
        self.status = '2'
        self.save()

    def arrive(self):
        self.status = '3'
        self.save()

    def end(self):
        self.status='4'
        self.is_running=False
        self.save()

    def next(parentRequest):
        return BusinessRequest.objects.filter(parentRequest=parentRequest, status='1')



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
