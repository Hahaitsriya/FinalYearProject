from django.shortcuts import render

# Create your views here.
# def wei(request):
#     return (render, 'dashboard.html')

def wei(request):
    #redirect to the index page.
    return render(request,'dashboard.html')

def hii(request):
    return render(request,'about.html')