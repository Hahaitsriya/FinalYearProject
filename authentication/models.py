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
    user_speciality = models.CharField(max_length=25,blank=True,null=False)

    def __str__(self):
        return self.username

class hospital(models.Model):
    hospital_name = models.CharField(max_length=500, null=True, blank=False)
    hospital_profile=models.ImageField(verbose_name="Hospital Profile",upload_to='media/hospital', null=True, blank=False)
    hospital_specialists = models.CharField(max_length=500,verbose_name="Hospital Speciality: ",null=True,blank=False)
    hospital_description=models.CharField(max_length=450,verbose_name="Explanation",blank=False, null=True)
    hospital_user = models.ManyToManyField(userProfile, related_name="user_hospital_details")
    def __str__(self):
        return self.hospital_name

    