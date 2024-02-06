from django.shortcuts import render
from authentication.models import userProfile
from django.http import HttpResponse ,HttpRequest

# Create your views here.
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
            #if user exists redirect to index html.
            return render(request,'index.html')
        else:
            #else show an error.
            error = "Username or password is incorrect."
    return render(request, 'login.html', {'error': error})
     
                    
#For displaying inital page for the viewers.
def home(request):
    #redirect to the index page.
    return render(request,'index.html')

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
# Add below existing imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

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