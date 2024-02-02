from django.db import models

# Create your models here.
class userProfile(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=150,verbose_name="Username",blank=True, null=False)
    user_email=models.EmailField(max_length=200, verbose_name="User Email", blank=True, null=False)
    user_contact=models.PositiveBigIntegerField(verbose_name="Contact number",blank=True,null=True)
    user_profile=models.ImageField(verbose_name="User Profile",upload_to='media')
    user_address=models.CharField(max_length=200,verbose_name="Address",blank=True,null=False)
    user_password=models.CharField(max_length=100,verbose_name="Password",blank=True,null=False)
    user_status=models.CharField(max_length=25,verbose_name="Status",blank=True,null=False)
