from django.shortcuts import render, redirect
from datetime import datetime, timedelta

from businesses.models import FoodItemClass, IndividualFoodItem
from .models import PickupRequest, BusinessRequest, Counter
from django.http import HttpResponse, HttpResponseRedirect
from businesses.models import Business, FoodItemClass
from clients.dieteryanalyzer import *
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
    if request.user.is_authenticated() and request.user.profile.is_client():
        businesses = Business.objects.all()
        return render(request, 'client/restaurants.html', {'businesses': businesses})
    else:
        return redirect('/login')
def viewRestaurant(request, business_id):
    if request.user.is_authenticated():
        business = Business.objects.get(id=business_id)
        items = FoodItemClass.get_list_available_for_business(business)
        return render(request, 'client/restaurant.html', {'business': business, 'user': request.user, 'items': items})
    else:
        return redirect('/login')

def list_restaurant_items(request, restaurant_id):
    if request.user.is_authenticated() and request.user.profile.is_client():
        restaurant = Business.objects.get(id=restaurant_id)
        items = IndividualFoodItem.get_available_for_business(restaurant)
        return render(request, 'client/restaurants.html', {'business': business, 'items': items})

    else:
        return redirect('/login')

def viewCart(request):
    if (request.user.is_authenticated() and request.user.profile.is_client()):
        items =  request.user.profile.client.cart.all()
        average = 0
        count=0
        for item in items:
            average += total_percent_deviation(get_from_percent_ideal(27.5, item.item_class.fat * 9, item.item_class.calories), get_from_percent_ideal(27.5, item.item_class.protein * 4, item.item_class.calories), get_from_percent_ideal(27.5, item.item_class.carbs * 4, item.item_class.calories))
            count+=1
        if count is not 0:
            average /= count
        else:
            average = 0
        return render(request, 'client/checkout.html', {'items': items,'deviation': average})
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
            business = item.item_class.business
            if (BusinessRequest.objects.filter(parentRequest=request, business=business).first() == None):
                new_br = BusinessRequest(business=business, parentRequest=request)
                new_br.save()

            br = BusinessRequest.objects.filter(parentRequest=request, business=business).first()
            br.items.add(item)
            br.save()

        return redirect('/clients/request/'+str(request.id))

    else:
        return redirect('/login')


def request(request, req_id):
    req = PickupRequest.objects.get(id=req_id)
    if (request.user.is_authenticated() and request.user.profile.is_client() and req.user == request.user):
        approve_button = (req.status == '2' and req.all_pickups_done())

        return render(request, 'client/request.html', {'request': req, 'approve_button': approve_button})

    else:
        return redirect('/login')


def approve(request, req_id):
    req = PickupRequest.objects.get(id=req_id)
    if (request.user.is_authenticated() and request.user.profile.is_client() and req.user == request.user and req.status == '2' and req.all_pickups_done()):
        req.status = '4'
        req.save()

        return redirect('/clients/')

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
