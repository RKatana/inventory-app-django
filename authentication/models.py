from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
<<<<<<< HEAD
from cloudinary.models import CloudinaryField

# Create your models here.

# class profile
class Profile(models.Model):
  profilePic = CloudinaryField('userProfile/', default='')
  username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  bio = HTMLField(blank=True, null=True)
  occupation = HTMLField(blank=True, null=True)
  phone = models.IntegerField(blank=True, null=True)
  count = models.IntegerField(default=0, null=True, blank=True)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(username=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.username.username
=======
from .managers import UserManager

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
        return self.name
>>>>>>> 9e956906a8ff7509db94fa0172500e00ca1ab070
