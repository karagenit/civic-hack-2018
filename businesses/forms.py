from django.contrib.auth.models import User, Group
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, UsernameField
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Business, PickupRequest, FoodItem


class AddItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Name'}))

    description = forms.CharField(label='Description', max_length=512, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Description'}))

    # May only contain alphabetical character

    # Save a new user and set their Group to Volunteer
    def save(self, commit=True):
        item = FoodItem(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
        )
        return item
