import uuid

from django.conf import settings
from django.db import models



# Create your models here.
   
class Store(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')

	
    
	def __str__(self):
		return self.name


    
    
