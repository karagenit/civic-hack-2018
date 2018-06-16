from django.shortcuts import render, redirect
from .forms import AddItemForm
from .models import Business, FoodItem

# Create your views here.
def test(request):
    return render(request, 'hi.html')

def home(request):
    business = Business.objects.get(profile=request.user.profile)
    return redirect('/businesses/viewItems/'+str(business.id))

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

def viewItems(request, biz_id):
    business = Business.objects.get(id=biz_id)
    items = FoodItem.objects.filter(business=business)
    return render(request, 'business/viewItems.html', {'business': business, 'items':items})

def addToItemCount(request, item_id):
    item = Item.objects.get(id=item_id)
    item.number = item.number + 1
    item.save()
    return redirect('/business/viewItems/'+str(item.business.id))

def subtractFromItemCount(request, item_id):
    item = Item.objects.get(id=item_id)
    item.number = item.number - 1
    item.save()
    return redirect('/business/viewItems/'+str(item.business.id))
