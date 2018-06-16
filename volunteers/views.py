from django.shortcuts import render

from .models import Volunteer

from clients.models import PickupRequest

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    if request.user.is_authenticated() and request.user.profile.is_driver():
        return redirect('/volunteers/requests/')

def requests(request):
    if request.user.is_authenticated() and request.user.profile.is_driver():
        pickuprequests = PickupRequest.objects.all()
        return render(request, 'volunteers/requests.html', {'requests': pickuprequests})
    elif request.user.is_authenticated():
        return HttpResponse(
            'You don\'t have the right permissions to see this page. You must be a Volunteer to access this page.')
    else:
        return redirect('/login')
        
def request(request, request_id):
    if request.user.is_authenticated():
        therequest = PickupRequest.objects.get(id=request_id)
        return render(request, 'volunteers/request.html', {'request': therequest})
    else:
        return redirect('/login')
