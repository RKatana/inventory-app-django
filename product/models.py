import uuid
from django.db import models
from store.models import Store
from authentication.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
  uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
  name =  models.CharField(max_length=200) 
  quantity = models.IntegerField(blank=True, null=True)
  buying_price = models.IntegerField(blank=True, null=True)
  selling_price = models.IntegerField(blank=True, null=True)
  spoilt = models.IntegerField(blank=True, null=True)
  payment_status = models.BooleanField(blank=True, null=True)
  date_received = models.CharField(max_length=199, blank=True, null=True)
  store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
