from django.shortcuts import render, redirect


# Sending user object to the form, to verify which fields to display/remove (depending on group)
def home(request):
    return render(request, 'index.html')
    if request.user.is_authenticated():
        user = request.user
        if (user.profile.is_client()):
            return redirect('/clients')
        elif (user.profile.is_restaurant()):
            return redirect('/businesses')
        elif (user.profile.is_driver()):
            return redirect('/volunteers')
        else:
            return redirect('/login')

    else:
        return redirect('/login')
