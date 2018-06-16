from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^viewItems/(?P<biz_id>[0-9]+)', views.viewItems),
    url(r'^addFoodItems/(?P<biz_id>[0-9]+)', views.addFoodItem),
    url(r'^deleteFoodItem/(?P<item_id>[0-9]+)', views.deleteFoodItem),
    url(r'^addToItemCount/(?P<item_class_id>[0-9]+)', views.addToItemCount),
    #url(r'^subtractFromItemCount/(?P<item_id>[0-9]+)', views.subtractFromItemCount),
    url(r'^restaurantfoods/', views.restaurantfoods),
    url(r'^$', views.home),
    url(r'^test/$', views.test),
    url(r'^drivertable/', views.drivertable),
    # edit item
    # view drivers
]
