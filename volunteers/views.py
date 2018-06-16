from django.shortcuts import render

from .models import Volunteer

from clients.models import PickupRequest

from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if request.user.is_authenticated() and request.user.profile.is_driver():
        return redirect('/volunteers/requests/')

def requests(request):
    if request.user.is_authenticated():
        pickuprequests = PickupRequest.objects.all()
        return render(request, 'volunteers/requests.html', {'requests': pickuprequests})
    else:
        return redirect('/login')

def request(request, request_id):
    if request.user.is_authenticated():
        therequest = PickupRequest.objects.get(id=request_id)
        return render(request, 'volunteers/request.html', {'request': therequest})
    else:
        return redirect('/login')
