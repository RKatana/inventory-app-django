from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    

    class Roles(models.TextChoices):
        Merchant = "Merchant", "merchant"
        Store_admin = "Store_admin", "store_admin"
        Clerk = "Clerk", "clerk"


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    role = models.CharField(max_length=255, choices= Roles.choices, blank=True, null=True, default=Roles.Clerk)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField(blank=True, null=True)
    modified_by = models.EmailField(blank=True, null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse ('user', kwargs={'pk': self.pk})

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email


class Merchant(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.Merchant
            self.set_password(self.password)
            self.email=self.email
        super(Merchant,self).save(*args, **kwargs)


class StoreAdmin(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.Store_admin
            self.set_password(self.password)
            self.email=self.email
        super(StoreAdmin,self).save(*args, **kwargs)


# class profile
class Profile(models.Model):
    profile_pic = CloudinaryField('image', default='image/upload/v1632754417/24-248253_user-profile-default-image-png-clipart-png-download_obstgc.png')
    username = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)


    @receiver(post_save, sender=get_user_model())
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(username=instance)

    # @receiver(post_save, sender=get_user_model())
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def __str__(self):
        return self.username.name

