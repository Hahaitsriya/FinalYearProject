# Generated by Django 4.2.9 on 2024-01-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_delete_doctor_delete_hospital_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(blank=True, max_length=150, verbose_name='Username')),
                ('user_email', models.EmailField(blank=True, max_length=200, unique=True, verbose_name='User Email')),
                ('user_contact', models.PositiveBigIntegerField(blank=True, verbose_name='Contact number')),
                ('user_profile', models.ImageField(upload_to='media', verbose_name='User Profile')),
                ('user_address', models.CharField(blank=True, max_length=200, verbose_name='Address')),
                ('user_password', models.CharField(blank=True, max_length=100, verbose_name='Password')),
                ('user_status', models.CharField(choices=[('user', 'User'), ('doctor', 'Doctor'), ('hospital', 'Hospital')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]