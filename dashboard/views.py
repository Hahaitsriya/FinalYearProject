from django.shortcuts import render
from dashboard.models import offerPost
from authentication.models import userProfile
from authentication.views import *

def base_home(request):
    # Retrieve user status from session
    user_status = request.session.get('user_status')
    context = {
        'user_status': user_status,
    }
    return render(request, 'base.html', context)

def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
    
        if request.method == 'POST':
            offer_title = request.POST.get('title')
            offer_body = request.POST.get('Body')
            today_date=request.POST.get('today_date')
            expiry_date=request.POST.get('expiry_Date')
            print(offer_title)

        offer_details=offerPost()

        offer_details.title = offer_title
        offer_details.Body=offer_body
        offer_details.today_date=today_date
    return render(request,'dashboard.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status})


# Create your views here.
# def offerPost(request):
    # user_id = request.session.get('user_id')
    # if user_id is None:
    #     return render(request,'login.html')
    # else:
    #     user_profile = userProfile.objects.get(user_id=user_id)
    #     if request.method == 'POST':
    #         offer_title = request.POST.get('title')
    #         offer_body = request.POST.get('Body')
    #         today_date=request.POST.get('today Date')
    #         expiry_date=request.POST.get('expiry_Date')
    #         print(offer_title)
    #     # printing the user status
    # return render(request,'dashboard.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status})
