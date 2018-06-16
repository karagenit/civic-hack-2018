from django.conf.urls import url
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^logout_lander/', views.logoutLander, name='logout_lander'),
    # url(r'^profile/$', views.profile, name='profile'),
    # url(r'^profile/(?P<user_id>[0-9]+)', views.other_profile, name="other_profile"),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    # url(r'^profile/edit/password/$', views.edit_password, name='edit_password'),
    url(r'^signupuser', views.signupUser, name='signupUser'),
    url(r'^signupclient', views.signupClient, name='signupClient'),
    url(r'^signupvolunteer', views.signupVolunteer, name='signupVolunteer'),
    url(r'^signupbusiness', views.signupBusiness, name='signupBusiness'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<user_id>[0-9]+)', views.other_profile, name="other_profile"),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
]
