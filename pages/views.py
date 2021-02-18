from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About</h1>")
