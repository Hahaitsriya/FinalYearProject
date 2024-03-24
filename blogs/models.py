from django.db import models
from authentication.models import userProfile

# Create your models here.
class blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title=models.CharField(max_length=50,verbose_name="title",null=False,blank=True)
    blog_body=models.TextField(max_length=3500,verbose_name="body",blank=True,null=False)
    blog_images=models.ImageField(verbose_name='Image for blog',upload_to="media/blog")
    blog_date=models.DateField(verbose_name='today_date',auto_now_add=True)
    user_id = models.ForeignKey(userProfile, on_delete=models.CASCADE)