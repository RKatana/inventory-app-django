# Generated by Django 3.2.8 on 2021-10-19 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_store_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='user',
        ),
    ]