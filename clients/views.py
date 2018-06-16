from django.shortcuts import render, redirect
from datetime import datetime, timedelta, timezone

from businesses.models import FoodItemClass, IndividualFoodItem
from .models import PickupRequest, Counter
from django.http import HttpResponse, HttpResponseRedirect
from businesses.models import Business, FoodItemClass

def home(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        return redirect('/clients/list')
    else:
        return redirect('/login')

def list_all_items(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        items = FoodItemClass.get_list_available()
        counter = Counter()
        print(items)
        return render(request, 'client/list_all.html', {'items': items, 'counter': counter})

    elif request.user.is_authenticated:
        return HttpResponse(
            'You don\'t have the right permissions to see this page. You must be a Client to access this page.')
    else:
        return redirect('/login')

def overallRestaurantView(request):
    businesses = Business.objects.all()
    return render(request, 'client/restaurants.html', {'businesses': businesses})

def viewRestaurant(request, business_id):
    if request.user.is_authenticated():
        business = Business.objects.get(id=business_id)
        items = FoodItemClass.get_list_available_for_business(business)
        return render(request, 'client/restaurant.html', {'business': business, 'user': request.user, 'items': items})
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
            item.status = '2'
            item.save()
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

def add_item_restaurant(request, item_id):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        item_class = FoodItemClass.objects.get(id=item_id)
        item = item_class.get_item()
        request.user.profile.client.cart.add(item)

        return redirect('/clients/restaurant/'+str(item_class.business.id))
    else:
        return redirect('/login')

def remove_item(request, item_id):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        item = IndividualFoodItem.objects.get(id=item_id)
        request.user.profile.client.cart.remove(item)

        return redirect('/clients/viewCart')

    else:
        return redirect('/login')
