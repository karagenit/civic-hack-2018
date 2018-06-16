from django.contrib.auth.models import User, Group
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, UsernameField
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Volunteer

from clients.models import Client, PickupRequest
