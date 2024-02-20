from django.shortcuts import render
from authentication.models import userProfile
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


# Create your views here.

#For displaying inital page for the viewers.
def home(request):
    #redirect to the index page.
    return render(request,'index.html')

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
            # print(user_status)
            #Saving into the session.
            request.session.save()
            #if user exists redirect to dashboard html.
            return render(request,'dashboard.html')
            # ,{'user_status':user_status}
        else:
            #else show an error.
            error = "Username or password is incorrect."
    return render(request, 'login.html', {'error': error}) 

def base_home(request):
    # Retrieve user status from session
    user_status = request.session.get('user_status')
    print(user_status)
    context = {
        'user_status': user_status,
        # Other context variables
    }
    return render(request, 'base.html', context)

# def base_home(request):
#     user_id=userProfile.user_id
#     if user_id in request.session:
#         userid=request.session['user_id']
#         print(userid)
#         status = userProfile.user_status
#     else:
#         print("qwertyuikl")
#         # user_id = request.session.get('user_id')
#     # user_Profile = userProfile.objects.get(user_id=userid)
#     # print(userid)
#     # user_id=userProfile.user_id
#     # print(user_id)
#     # status = user_Profile.user_status
#     # print(status)
#     user_profile = userProfile.objects.get(user_id=user_id)
#     return render(request,'base.html',{'status':status})

#For displaying inital page for the viewers.
# def home(request):
    # userid = request.session.get('user_id')
    # user_Profile = userProfile.objects.get(user_id=userid)
    # print(userid)
    # status = user_Profile.user_status
    # print(status)
    #redirect to the index page.
    # return render(request,'index.html')

def dashboard(request):
     # Call the base_home view to get the base functionality
    base_context = base_home()
     # Merge the base context with the dashboard.
    context = {**base_context}
    userid = request.session.get['user_id']
    user_Profile = userProfile.objects.get(user_id=userid)
    print(userid)
    status = user_Profile.user_status
    print(status)
    # Render the dashboard template with the merged context
    return render(request, 'dashboard.html', {'status':status}, context)


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
        print(status)
        #Saves the data.
        user.save()
    return render(request,'signup.html')

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


# so we can reference the user model as User instead of CustomUser
# user = userProfile()

# send email with verification link
# def verify_email(request):
#     if request.method == "POST":
#         if request.user.email_is_verified != True:
#             current_site = get_current_site(request)
#             user = request.username
#             email = request.user.email
#             subject = "Verify Email"
#             message = render_to_string('user/verify_email_message.html', {
#                 'request': request,
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             email = EmailMessage(
#                 subject, message, to=[email]
#             )
#             email.content_subtype = 'html'
#             email.send()
#             return render('verify-email-done')
#         else:
#             return render('signup')
#     return render(request, 'user/verify_email.html')