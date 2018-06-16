from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^requests/', views.requests, name = 'requests'),
    url(r'^request/(?P<request_id>[0-9]+)', views.request, name = 'request')
]
