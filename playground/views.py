from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def say_hello(request):
    return HttpResponse('Hello World')
