# Generated by Django 3.2.8 on 2021-10-20 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='store',
        ),
    ]
