from django.shortcuts import render
from authentication.models import User,Doctor,Hospital
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def login(request):
    return render(request,'login.html')