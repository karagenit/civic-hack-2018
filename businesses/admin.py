from django.contrib import admin
from .models import Business, IndividualFoodItem, FoodItemClass

admin.site.register(Business)
admin.site.register(FoodItemClass)
admin.site.register(IndividualFoodItem)
