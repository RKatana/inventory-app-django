from django.conf import settings
from django.db import models
from authentication.models import User


# Create your models here.
   
class Store(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
    
	def __str__(self):
		return self.name


    
    
