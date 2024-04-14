from django.shortcuts import render,redirect, get_object_or_404
from authentication.models import userProfile
from dashboard.models import offerPost
from django.http import HttpResponse ,HttpRequest
import json
# Add below existing imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from blogs.models import blogs
import random


# Create your views here.

#For displaying inital page for the viewers.
def home(request):
     # Retrieve all blog posts
    all_posts = blogs.objects.all()

    if all_posts:
        # Select a random blog post
        random_post = random.choice(all_posts)
    else:
        random_post = None
    #redirect to the index page.
    return render(request,'index.html', {'random_post': random_post})

#For users to login.
def login(request):
    error = ""
    #Fetch the data from login form into the variable using post method.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = userProfile.objects.filter(username=username, user_password=password).exists() 
        #To check if a user with the given username and password exists.
        #There is use of filter and exists methods.

        if user:
            user_Profile = userProfile.objects.get(username=username, user_password=password)
            # Fetching all the data into the sessions.
            request.session['user_id'] = user_Profile.user_id
            request.session['status'] = user_Profile.user_status
            user_status = user_Profile.user_status

            #Saving into the session.
            request.session.save()

            #if user exists redirect to dashboard url.
            return redirect('dashboard')
        else:
            #else show an error.
            error = "Username or password is incorrect."
    return render(request, 'login.html', {'error': error}) 

def signup(request):
    #Fetch data from html and css form. 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact=request.POST.get('contact')
        email=request.POST.get('email_Address')
        address=request.POST.get('home_Address')
        image=request.POST.get('image_upload')
        status=request.POST.get('status')
        if status == 'doctor':
            specification_doctor = request.POST.get('specification_doctor')

        # Loading the feilds from authentication.models(userProfile) into the variable user. 
        user=userProfile()

        #Loading the data from into the database.
        user.username = username
        user.user_password = password
        user.user_contact=contact
        user.user_email=email
        user.user_address=address
        user.user_profile=image
        user.user_status =status
        user.user_speciality=specification_doctor
        #Saves the data.
        user.save()
    return render(request,'signup.html')

def profile(request, user_id):
    # Fetch the userProfile object based on the provided user ID
    user_profile = get_object_or_404(userProfile, user_id=user_id)
    
    # No need to check session user_id here, as user_id is provided as a parameter
    
    # Printing the user status (you need to use user_profile.username, not userProfile.username)
    print(user_profile.username)
    
    return render(request, 'profile.html', {'username': user_profile.username, 
                                            'status': user_profile.user_status, 
                                            'email': user_profile.user_email, 
                                            'contact': user_profile.user_contact, 
                                            'user_profile': user_profile})

# send email with verification link
def verify_email(request):
    # so we can reference the user model as User instead of CustomUser
    user = userProfile()
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.username
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('user/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return render('verify-email-done')
        else:
            return render('signup')
    return render(request, 'user/verify_email.html')

def about_page(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
        offer_detail=offerPost.objects.all()
        print(offer_detail)
    return render(request,'about.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'offer_detail':offer_detail})