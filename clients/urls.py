from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^viewItems/(?P<biz_id>[0-9]+)', views.viewItems),
    url(r'^requestFood/', views.addClientRequest)
    url(r'^restaurantfoods/', views.restaurantfoods),
    # edit item
    # view drivers
]
