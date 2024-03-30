from django.shortcuts import render
from .models import userProfile
from blogs.models import blogs
from datetime import date
import random

# Create your views here.
def blog_upload(request):
    user_id = request.session.get('user_id')
    user_profile = userProfile.objects.get(user_id=user_id)
    
    if request.method == 'POST':
        title = request.POST.get('title_blog')
        body = request.POST.get('body_blog')
        images = request.POST.get('blog_picture')
    
        blog_details = blogs(user_id=user_profile, blog_title=title, blog_body=body, blog_images=images)
        blog_details.save()
        print(blog_details)
    
    return render(request,'blog/upload_blog.html', {'user_id': user_id, 'blog_date': date.today()})

def blog(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return render(request,'login.html')
    else:
        user_profile = userProfile.objects.get(user_id=user_id)
        blog_details=blogs.objects.all()
        print(blog_details)
    return render(request,'blog/blog.html',{'username':user_profile.username,'user_id':user_id,'status':user_profile.user_status,'blog_details':blog_details})


# def random_post(request):
#     # Fetch all posts
#     all_posts = blogs.objects.get('blog_title')
#     print(all_posts)
    

#     return render(request, 'index.html', {'all_posts': all_posts})
   