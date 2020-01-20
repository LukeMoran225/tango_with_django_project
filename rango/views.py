from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<p>Rango says hey there partner!</p>"
                        "<p>Visit the <a href='/rango/about'>About</a> page for more info!</p>")

def about(request):
    return HttpResponse("<p>Rango says here is the about page.</p>"
                        "<p>Return to the <a href='/rango/'>Index</a> page if you like! </p>")

