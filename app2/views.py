from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pooja(request):
    return HttpResponse('nothing is permanent in this world')

def purna(request):
    return render (request,'naru.html')
