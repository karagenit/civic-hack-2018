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

    objects = models.Manager()

    @receiver(post_save, sender=Profile)
    def create_user_business(sender, instance, **kwargs):
        if instance.member_type == '3':
            Business.objects.create(profile=instance)

    @receiver(post_save, sender=Profile)
    def save_user_business(sender, instance, **kwargs):
        #TODO: should be able to delete all the except: stuff after all the users have run this
        if instance.member_type == '3':
            instance.business.save()




class FoodItemClass(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
    )

    # def get_number_available(self):
    #     if (IndividualFoodItem.objects.filter(item_class=self).filter(status='1') == None):
    #         return 0
    #     else:
    #         return IndividualFoodItem.objects.filter(item_class=self).filter(status='1').count()


    def get_items_classes_for_business(business):
        item_classes = FoodItemClass.objects.filter(business=business)
        return item_classes

    def get_count(self):
        if (IndividualFoodItem.objects.filter(item_class=self) == None):
            return 0
        else:
            return IndividualFoodItem.objects.filter(item_class=self).count()

    def get_count_available(self):
        if (IndividualFoodItem.objects.filter(item_class=self).filter(status='1') == None):
            return 0
        else:
            return IndividualFoodItem.objects.filter(item_class=self).filter(status='1').count()



    def get_item(self):
        return IndividualFoodItem.objects.filter(item_class=self, status='1').first()

    def get_list_available():
        list = []

        for item_class in FoodItemClass.objects.all():
            if (item_class.get_item() != None):
                list.append(item_class)

        return list

    def get_list_available_for_business(business):
        list = FoodItemClass.get_list_available()

        for item_class in list:
            if (item_class.business != business):
                list.remove(item_class)

        return list




class IndividualFoodItem(models.Model):
    item_class = models.ForeignKey(
        FoodItemClass,
        on_delete=models.CASCADE,
    )
    STATUS_CHOICES = (('1', 'Available',), ('2', 'Requested',))
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def get_available():
        items = IndividualFoodItem.objects.filter(status='1')
        return items

    def get_available_for_business(business):
        business_item_classes = FoodItemClass.objects.filter(business=business)
        items = None
        for item_class in business_item_classes:
            if (items != None):
                items = items | IndividualFoodItem.objects.filter(status='1', item_class=item_class)
            else:
                items = IndividualFoodItem.objects.filter(status='1', item_class=item_class)

        return items
