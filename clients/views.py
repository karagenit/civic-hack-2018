from django.shortcuts import render

from .forms import 
# Create your views here.

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
