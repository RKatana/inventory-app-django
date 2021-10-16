from django.db import models
from store.models import Store
# Create your models here.

class Product(models.Model):
  name =  models.CharField(max_length=200) 
  quantity = models.IntegerField(blank=True, null=True)
  buying_price = models.IntegerField(blank=True, null=True)
  selling_price = models.IntegerField(blank=True, null=True)
  spoilt = models.IntegerField(blank=True, null=True)
  payment_status = models.BooleanField(blank=True, null=True)
  date_upload = models.DateTimeField(auto_now_add=True)
  store = models.ManyToManyField( Store )

  def save_product(self):
    self.save()

  @classmethod
  def delete_product(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def update_product(cls, id, productchange):
    cls.objects.filter(id = id).update(product = productchange)

  @classmethod
  def get_products_by_id(cls, id):
    try:
      product = cls.objects.get(id=id)
      return product
    except Product.DoesNotExist:
      print('Product does not exist')
      
  def __str__(self):
    return self.product_name
