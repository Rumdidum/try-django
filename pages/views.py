from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {"Infos": "give me some infos", "random_number": 34}
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})