from django.shortcuts import render
from .models import userProfile
from blogs.models import blogs
from datetime import date

# Create your views here.
def blog_upload(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    
    user_id = request.session.get('user_id')
    for_profile = userProfile.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        title = request.POST.get('title_blog')
        body = request.POST.get('body_blog')
        images = request.POST.get('blog_picture')
    
        blog_details = blogs(user_id=user_profile, blog_title=title, blog_body=body, blog_images=images)
        blog_details.save()
        print(blog_details)
    
    return render(request,'blog/upload_blog.html', {'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'user_profile':user_profile.user_profile, 'blog_date': date.today(),'profile_pp':for_profile.user_profile})

def blog(request):
    user_id = request.session.get('user_id')
    user_id = request.session.get('user_id')
    for_profile = userProfile.objects.get(user_id=user_id)
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
        blog_details=blogs.objects.all()
        print(blog_details)
    return render(request,'blog/blog.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'user_profile':user_profile.user_profile,'blog_details':blog_details,'profile_pp':for_profile.user_profile})
