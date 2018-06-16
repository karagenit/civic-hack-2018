from django.shortcuts import render, redirect


# Sending user object to the form, to verify which fields to display/remove (depending on group)
def home(request):
    return render(request, 'index.html')
