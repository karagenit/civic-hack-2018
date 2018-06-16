from django.contrib.auth.models import User, Group
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, SetPasswordForm, AuthenticationForm, UsernameField
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Business, FoodItemClass


class AddItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Name'}))

    description = forms.CharField(label='Description', max_length=512, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control form',
               'placeholder': 'Description'}))
    fat = forms.IntegerField(label='Fat g', widget=forms.NumberInput(
      attrs={ 'type': 'number',
              'max': '20',
              'class': 'form-control form',
              'placeholder': 'Grams of Fat'}))
    carbs = forms.IntegerField(label='Carbs g', widget=forms.NumberInput(
      attrs={ 'type': 'number',
              'max': '400',
              'class': 'form-control form',
              'placeholder': 'Grams of Carbohydrates'}))
    protein = forms.IntegerField(label='Protein g', widget=forms.NumberInput(
      attrs={ 'type': 'number',
              'max': '60',
              'class': 'form-control form',
              'placeholder': 'Grams of Protein'}))
    calories = forms.IntegerField(label='Calories', widget=forms.NumberInput(
      attrs={ 'type': 'number',
              'max': '3000',
              'class': 'form-control form',
              'placeholder': 'Calories'}))


    # May only contain alphabetical character

    # Save a new user and set their Group to Volunteer
    def save(self, commit=True):
        item = FoodItemClass(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            carbs=self.cleaned_data['carbs'],
            fat=self.cleaned_data['fat'],
            protein=self.cleaned_data['protein'],
            calories=self.cleaned_data['calories']
        )
        return item
