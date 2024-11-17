from django.shortcuts import render
from . models import passenger

# Create your views here.

def index(request):
    passenger_list = passenger.objects.all()
    return render(request, 'airline/index.html', {'passenger_list': passenger_list})

def search(request):
    pass
