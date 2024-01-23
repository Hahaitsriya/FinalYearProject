from django.shortcuts import render
from login.models import User,Doctor,Hospital
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def login(request):
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('signup_username')
        password = request.POST.get('signup_password')
        contact=request.POST.get('contact')
        email=request.POST.get('email_Address')
        # status=request.POST.get('signup_status')
        print('sucessful')
        # print(status)
        print(username)
        # if status=="users":
        #     usermodel = User()
        #     usermodel.Username = username
        #     usermodel.User_email = email
        #     usermodel.User_contact = contact
        #     usermodel.User_password = password
        #     usermodel.User_status = "users"
        #     usermodel.save()
        #     print('sucessful')
        # elif status =="doctor":
        #     datamodel=Doctor()
        #     datamodel.save()
        # else:
        #     datamodel=Hospital()
        #     datamodel.save()
    return render(request,'signup.html') 

        