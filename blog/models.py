from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)