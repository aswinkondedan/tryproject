
from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def homefunction(request):
    return HttpResponse("welcome")

def aboutfunction(request):
    return HttpResponse('<h1>about</h1>')

def designfunction(request):
    return render(request,'design.html')
