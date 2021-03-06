# Generated by Django 3.2.8 on 2021-10-12 14:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_profilepic_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='image/upload/v1632754417/24-248253_user-profile-default-image-png-clipart-png-download_obstgc.png', max_length=255, verbose_name='image'),
        ),
    ]
