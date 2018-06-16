from django.shortcuts import render
from .forms import AddItemForm
from .models import Business

# Create your views here.
def addFoodItem(request, biz_id):
    business = Business.objects.get(id=biz_id)
    if(request.method == 'POST'):
        form = AddItemForm(request.POST)
        # Makes sure the user filled out the form correctly as dictated by forms.py
        if form.is_valid():
            item = form.save(commit=False)
            item.business = business
            item.save()

            return redirect('/business/viewItems/'+str(business.id))
    else:
        form1 = SignupForm()
        form2 = EditProfileForm()

    return render(request, 'accounts/signupuser.html', {'form1': form1, 'form2': form2})

def viewItems(request, biz_id):
    business = Business.objects.get(id=biz_id)
    items = FoodItem.objects.filter(business=business)
    return render(reqeuest, 'business/viewItems.html', {'business': business, 'items':items})

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

def restaurantfoods(request):
    return render(request, 'restaurantfoods.html')
