from django.db import models
from django.utils import timezone
from authentication.models import userProfile

# Create your models here.
class offerPost(models.Model):
    offer_id=models.AutoField(primary_key=True,unique=True)
    offer_title=models.CharField(max_length=50,verbose_name="title",null=False,blank=True)
    offer_body=models.TextField(max_length=2500,verbose_name="Body",blank=True,null=False)
    today_date=models.DateField(verbose_name="today_date", auto_now_add=True)
    expiry_date=models.DateField(verbose_name="expiry_Date", blank=True, null=False,default=timezone.now)
    # offer_picture=models.ImageField(verbose_name="Post Image",upload_to='media\media\offerPost')
    user_id = models.ForeignKey(userProfile, on_delete=models.CASCADE)

    

    