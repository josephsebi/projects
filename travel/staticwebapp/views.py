from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.

def demo(request):
    place=Place.objects.all()
    return render(request, 'index.html',{'output':place})

def home(request):
    team=Team.objects.all()
    return render(request, 'index.html',{'result':team})






