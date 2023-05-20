from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rahul(request):
    return HttpResponse('<h1><marquee>haiii everyone</h1></marquee>')