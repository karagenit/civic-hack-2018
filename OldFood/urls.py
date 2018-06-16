"""OldFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from businesses.models import Business

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
<<<<<<< HEAD
    url(r'^$', auth_views.login, {'template_name':'accounts/login.html'}),
    url(r'^businesses/', include('businesses.urls', namespace='businesses'))
=======
    url(r'^login', auth_views.login, {'template_name':'accounts/login.html'}),
    url(r'^businesses/', include('businesses.urls')),
    url(r'^$', views.home),

>>>>>>> e26a6ee8e155301f23a09a34f91da87013e8d03b

]
