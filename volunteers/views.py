from django.shortcuts import render

from .models import Volunteer

from clients.models import PickupRequest

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
last_location = None


def home(request):
    if request.user.is_authenticated() and request.user.profile.is_driver():
        return redirect('/volunteers/requests/')

def requests(request):
    if request.user.is_authenticated() and request.user.profile.is_driver():
        pickuprequests = PickupRequest.objects.filter(driver=None)
        return render(request, 'volunteers/requests.html', {'requests': pickuprequests})
    elif request.user.is_authenticated():
        return HttpResponse(
            'You don\'t have the right permissions to see this page. You must be a Volunteer to access this page.')
    else:
        return redirect('/login')

def addRequest(request, request_id):
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

def accept(request, request_id):
    req = PickupRequest.objects.get(id=request_id)
    if request.user.is_authenticated() and request.user.profile.is_driver() and req.driver == None:
        req.driver = request.user.profile.volunteer
        req.accept()
        req.save()

        return redirect('/volunteers/drive/'+str(req.id))
    return redirect('/login')

def drive(request, request_id):
    home = False
    arrived = False
    req = PickupRequest.objects.get(id=request_id)
    if (request.user.profile.volunteer.last_location == None):
        get_loc(request.user.profile.volunteer)

    if request.user.is_authenticated() and request.user.profile.is_driver() and req.driver == request.user.profile.volunteer:
        if req.current() != None:
            current = req.current()
        else:
            current = req.next_business_request()
            if (current != None):
                current.start()
            else:
                home = True
        if not home:
            arrived = (current.status == '3')

        return render(request, 'volunteers/drive.html', {'request': req, 'current': current, 'arrived': arrived, 'home':home, 'last_location': request.user.profile.volunteer.last_location})
    return redirect('/login')

def arrived(request, request_id):
    req = PickupRequest.objects.get(id=request_id)
    if request.user.is_authenticated() and request.user.profile.is_driver() and req.driver == request.user.profile.volunteer:
        req.current().arrive()

        return redirect('/volunteers/drive/'+str(req.id))
    return redirect('/login')

def deliver(request, request_id):
    req = PickupRequest.objects.get(id=request_id)
    if request.user.is_authenticated() and request.user.profile.is_driver() and req.driver == request.user.profile.volunteer:
        req.status = '3'
        req.save()

        return redirect('/volunteers/')
    return redirect('/login')

def picked_up(request, request_id):
    req = PickupRequest.objects.get(id=request_id)
    if request.user.is_authenticated() and request.user.profile.is_driver() and req.driver == request.user.profile.volunteer:
        request.user.profile.volunteer.last_location = req.current().business.address
        request.user.profile.volunteer.save()
        req.current().end()

        return redirect('/volunteers/drive/'+str(req.id))
    return redirect('/login')


def get_loc(volunteer):
    volunteer.last_location('Union 525, Indianapolis, IN')
    volunteer.save()
