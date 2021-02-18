from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")

def about_view(*args, **kwargs):
    return HttpResponse("<h1>About</h1>")
