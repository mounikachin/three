from django.shortcuts import render
from django.http import *

# Create your views here.
def jamapandu(request):
    return HttpResponse('<h1><marquee>hi hello</h1></marquee>') 

def mounika(request):
    return HttpResponse('<h1><marquee> heloo</h1></marquee>')




