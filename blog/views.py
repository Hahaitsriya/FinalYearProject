# from django.shortcuts import render
# from blog.models import blog
# from blog.forms import blogform
# from authentication.models import userProfile

# def upload_blog(request):
#     user_id = request.session.get('user_id')
#     user_profile = userProfile.objects.get(user_id=user_id)
#     if request.method == 'POST':
#         form= blogform()
#         if  form.is_valid():
#             form.save()    
#     context={
#          'form':form
#      }   
#     return render(request,'blog/upload_blog.html',context=context)
            
        
    
    
