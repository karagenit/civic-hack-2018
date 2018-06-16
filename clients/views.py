from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def list_all_items(request):
    if (request.user.is_authenticated() && request.user.profile.is_client()):
        items = IndividualFoodItem.get_available()
        return redirect('/client')

    else:
        return redirect('/login')

from .forms import 
# Create your views here.
<<<<<<< HEAD
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
=======

def addClientRequest(request):
    client = Client.objects.get(profile=request.user.profile)
    if(request.method == 'POST'):
        form = AddItemForm(request.POST)
        # Makes sure the user filled out the form correctly as dictated by forms.py
        if form.is_valid():
            item = form.save(commit=False)
            item.business = business
            item.save()

            return redirect('/businesses/viewItems/'+str(business.id))
    else:
        form = AddItemForm()


    return render(request, 'business/addFoodItem.html', {'form': form})
>>>>>>> 30856e3f85e7638371e56b4ab6eed4a15cb34768
