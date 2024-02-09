# Generated by Django 4.2.9 on 2024-02-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_userprofile_user_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Username',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(blank=True, max_length=200, verbose_name='User Email'),
        ),
    ]