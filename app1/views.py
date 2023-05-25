from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def simha(request):
    return HttpResponse('everything is temporary')

def naru(request):
    return render(request,'happy.html')