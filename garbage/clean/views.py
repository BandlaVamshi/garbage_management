from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

b = []
def index(request):
    return render(request, 'clean/index.html')

def next(request):
    return render(request,'clean/first.html')

def results(request):
    a = []
    c = []
    current = data.objects.all()
    if len(current) == 1:
        for i in current:
            a.append(int(i.sensor1))
            a.append(int(i.sensor2))
            a.append(int(i.sensor3))
            c.append(float(i.city_latitude))
            c.append(float(i.city_longitude))
    print a
    print c
    context = {
    "aa":a,
    "bb":c,
    }
    return render(request,'clean/results.html',context)
def store(request,city,latitude,longitude,sens1,sens2,sens3):
    current = data.objects.all()
    current.delete()

    cu = data(city_name = city,city_latitude = latitude, city_longitude = longitude,sensor1 = sens1,sensor2 = sens2,sensor3 = sens3)
    cu.save()
    return HttpResponse("Inserted")

def Location(request):
    print b
    context ={
    "aa":b,
    }
    return render(request,'clean/maps.html',context)
