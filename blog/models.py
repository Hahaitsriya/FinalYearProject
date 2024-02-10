from django.db import models

# Create your models here.
class dashboard(models.Model):
    title=models.CharField(max_length=50,verbose_name="title",null=False,blank=True)
    body=models.TextField(max_length=2500,verbose_name="Body",blank=True,null=False)
    