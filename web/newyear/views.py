from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Kolkata')
today = datetime.now(timezone)

def is_newyear():
    return datetime.now().month == 1 and datetime.now().day == 1

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the newyear index.</h1>")

def newyear(request):
    if is_newyear():
        year = today.year
        return render(request, 'newyear/index.html',
                    {'year': year}
                    )
    else:
        return render(request, 'newyear/date.html',
                    {'date': today.strftime('%Y-%m-%d')}
                    )