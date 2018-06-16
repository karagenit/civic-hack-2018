from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^requests/', views.requests, name = 'requests'),
    url(r'^request/(?P<request_id>[0-9]+)', views.request, name = 'request'),
    url(r'^accept/(?P<request_id>[0-9]+)', views.accept, name = 'accept'),
    url(r'^arrived/(?P<request_id>[0-9]+)', views.arrived, name = 'arrived'),
    url(r'^picked_up/(?P<request_id>[0-9]+)', views.picked_up, name = 'picked_up'),
    url(r'^drive/(?P<request_id>[0-9]+)', views.drive, name = 'drieve'),
    url(r'^deliver/(?P<request_id>[0-9]+)', views.deliver, name = 'deliver'),
]
