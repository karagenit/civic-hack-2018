from django.shortcuts import render, redirect
from .forms import AddItemForm
from .models import Business, FoodItemClass, IndividualFoodItem

# Create your views here.
def test(request):
    return render(request, 'hi.html')

def home(request):
    if (request.user.is_authenticated() and request.user.profile.is_restaurant()):
        business = Business.objects.get(profile=request.user.profile)
        return redirect('/businesses/viewItems/'+str(business.id))
    else:
        return redirect('/login')

def addFoodItem(request, biz_id):
    business = Business.objects.get(id=biz_id)
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

def deleteFoodItem(request, item_id):
    item = FoodItemClass.objects.get(id=item_id)
    if(request.user.is_authenticated() and request.user.profile.is_restaurant() and item.business==request.user.profile.business):
        item.delete()
        return redirect('/businesses')
    else:

        return redirect('/login')

def viewItems(request):
    business = Business.objects.get(profile=request.user.profile)
    items = FoodItemClass.get_items_classes_for_business(business)
    return render(request, 'business/viewItems.html', {'business': business, 'items':items})

def addToItemCount(request, item_class_id):
    item_class = FoodItemClass.objects.get(id=item_class_id)
    item = IndividualFoodItem(item_class=item_class, status='1')
    item.save()
    return redirect('/businesses/')

def subtractFromItemCount(request, item_id):
    item_class = FoodItemClass.objects.get(id=item_id)
    item = item_class.get_item()

    if (item != None):
        item.delete()

    return redirect('/businesses')


def restaurantfoods(request):
    return render(request, 'restaurantfoods.html')

def drivertable(request):
    return render(request, 'drivertable.html')
