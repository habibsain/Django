from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the newyear index.</h1>")

# Create your views here.
