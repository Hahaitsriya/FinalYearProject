from django.shortcuts import render
from dashboard.models import offerPost
from authentication.models import userProfile
from authentication.views import *
from datetime import date

def base_home(request):
    # Retrieve user status from session
    user_status = request.session.get('user_status')
    context = {
        'user_status': user_status,
    }
    return render(request, 'base.html', context)

def post_dashboard(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
            title = request.POST.get('title')
            body = request.POST.get('Body')
            explaination=request.POST.get('explaination')
            location=request.POST.get('location')
            due_date=request.POST.get('expiry_date')
            # offer_image=request.POST.get('offer_picture')
        
            # Create an instance of OfferPost and assign the user_profile to user_id field
            offer_details = offerPost(user_id=user_profile, offer_title=title, offer_body=body,offer_explaination=explaination,offer_location=location,today_date=date.today(),expiry_date=due_date)
            offer_details.save()
    return render(request,'dashboard/upload_dashboard.html',{'user_id':user_id,'today_date':date.today()})

def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
        offer_detail=offerPost.objects.all()
        print(offer_detail)
        # print(titles)
    return render(request,'dashboard/dashboard.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'offer_detail':offer_detail})
