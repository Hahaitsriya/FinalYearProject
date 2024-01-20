from django.shortcuts import render
from login.models import User,Doctor,Hospital
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def login(request):
    return render(request,'login.html')