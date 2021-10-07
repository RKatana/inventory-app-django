from django.db import models
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