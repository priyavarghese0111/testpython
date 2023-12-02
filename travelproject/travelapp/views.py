from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import People

# Create your views here.

def demo(request):
    obj = Place.objects.all()
    test = People.objects.all()
    return render(request,'index.html',{'result':obj,'change':test})

