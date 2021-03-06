# Generated by Django 3.2.8 on 2021-10-18 10:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='address',
        ),
        migrations.RemoveField(
            model_name='store',
            name='city',
        ),
        migrations.AddField(
            model_name='store',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Public identifier'),
        ),
    ]
