# Generated by Django 4.2.9 on 2024-02-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_userprofile_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_status',
            field=models.CharField(blank=True, max_length=25, verbose_name='Status'),
        ),
    ]
