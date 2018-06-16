from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def list_all_items(request):
    if (request.user.is_authenticated() && request.user.profile.is_client()):
        items = IndividualFoodItem.get_available()
        return redirect('/client')

    else:
        return redirect('/login')

# Create your views here.
def checkout(request):
    if (request.user.is_authenticated() && request.user.profile.is_client()):
        client = request.user.profile.client
        request = PickupRequest(user=request.user, date_created=datetime.now())
        cart = client.cart
        for (item in cart):
            request.items.add(item)
            cart.remove(item)
        cart.clear()
        client.save()

        request.save()

        return redirect('/client')

    else:
        return redirect('/login')




def add_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)

    if (request.user.is_authenticated() && request.user.profile.is_client()):
        request.user.profile.client.cart.add(item)

        return redirect('/client')

    else:
        return redirect('/login')

def remove_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)

    if (request.user.is_authenticated() && request.user.profile.is_client()):
        request.user.profile.client.cart.remove(item)

        return redirect('/client')

    else:
        return redirect('/login')
