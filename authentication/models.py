from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .managers import UserManager
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse ('user', kwargs={'pk': self.pk})

    def get_email(self):
        return self.email

    def __str__(self):
        if self.name:
            return self.name
        return self.email


# class profile
class Profile(models.Model):
    profile_pic = CloudinaryField('userProfile/', default='')
    username = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(default=0, null=True, blank=True)
    date_upload = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=get_user_model())
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(username=instance)

    # @receiver(post_save, sender=get_user_model())
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def __str__(self):
        return self.username.name

