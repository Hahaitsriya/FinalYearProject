from django.shortcuts import render
from dashboard.models import offerPost
from authentication.models import userProfile
from authentication.views import *
from datetime import date
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

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
            offer_image=request.POST.get('offer_picture')
        
            # Create an instance of OfferPost and assign the user_profile to user_id field
            offer_details = offerPost(user_id=user_profile, offer_title=title, offer_body=body,offer_explaination=explaination,offer_location=location,today_date=date.today(),expiry_date=due_date, offer_picture=offer_image)
            offer_details.save()
    return render(request,'dashboard/upload_dashboard.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'today_date':date.today()})

@login_required
def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
        today_date = timezone.now()
        offer_detail = offerPost.objects.filter(expiry_date__gte=today_date)
    
    return render(request,'dashboard/dashboard.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'offer_detail':offer_detail})

@login_required
def user_doctor(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    profiles = userProfile.objects.filter(user_status="doctor")
    return render(request, 'user_doctor.html', {'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'profiles': profiles})
    
@login_required
def register_view(request, pk):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('user_email')
        user_contact=request.POST.get('contact')
        
        # Send email to user
        user_subject = 'Registration Confirmation'
        user_message = f'Hi {username},\n\nThank you for registering with us!\n\nYour participation in this event has been successfully registered.'
        send_mail(user_subject, user_message, email, [email])

        # Fetch admin email from offer detail
        offer =  offerPost.objects.get(offer_id=pk)
        admin_email = offer.user_id.user_email  
        
          # Send email to admin
        admin_subject = 'New User Registration'
        admin_message = f'A new user has registered:\n\nUsername: {username}\nEmail: {email}\nContact: {user_contact}'
        send_mail(admin_subject, admin_message, admin_email, [admin_email])

              # Assuming registration is successful, send a success message
        message = 'Registration successful'
        return redirect('dashboard')
    
    
    