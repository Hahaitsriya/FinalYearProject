# Generated by Django 4.2.9 on 2024-01-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_delete_doctor_delete_hospital_alter_user_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_profile',
            field=models.ImageField(upload_to='static/pictures', verbose_name='User Profile'),
        ),
    ]
