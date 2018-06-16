from django.shortcuts import render, redirect
from datetime import datetime, timedelta, timezone

from businesses.models import FoodItemClass, IndividualFoodItem
from .models import PickupRequest

def home(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        return redirect('/clients/list')
    else:
        return redirect('/login')

def list_all_items(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        items = FoodItemClass.get_list_available()
        print(items)
        return render(request, 'client/list_all.html', {'items': items})

    else:
        return redirect('/login')

def restaurants(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        businesses = Business.objects.all()
        return render(request, 'client/restaurants.html', {'businesses': businesses})

    else:
        return redirect('/login')

def list_restaurant_items(request, restaurant_id):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        restaurant = Business.objects.get(id=restaurant_id)
        items = IndividualFoodItem.get_available_for_business(restaurant)
        return render(request, 'client/restaurants.html', {'business': business, 'items': items})

    else:
        return redirect('/login')

def viewCart(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        items =  request.user.profile.client.cart.all()
        return render(request, 'client/checkout.html', {'items': items})
    else:
        return redirect('/login')


# Create your views here.
def checkout(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        client = request.user.profile.client
        request = PickupRequest(user=request.user, date_created=datetime.now())
        request.save()
        cart = client.cart
        for item in cart.all():
            request.items.add(item)
            cart.remove(item)
        cart.clear()
        client.save()

        request.save()

        return redirect('/clients')

    else:
        return redirect('/login')


def add_item(request, item_id):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        item_class = FoodItemClass.objects.get(id=item_id)
        item = item_class.get_item()
        request.user.profile.client.cart.add(item)

        return redirect('/clients')

    else:
        return redirect('/login')

def remove_item(request, item_id):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        item = IndividualFoodItem.objects.get(id=item_id)
        request.user.profile.client.cart.remove(item)

        return redirect('/clients/viewCart')

    else:
        return redirect('/login')
