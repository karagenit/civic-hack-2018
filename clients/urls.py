from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^list/$', views.list_all_items),
    url(r'^addToCart/(?P<item_id>[0-9]+)/$', views.add_item),
    url(r'^removeFromCart/(?P<item_id>[0-9]+)/$', views.remove_item),
    url(r'^viewCart/$', views.viewCart),
    url(r'^checkout/$', views.checkout),

    # edit item
    # view drivers
]
