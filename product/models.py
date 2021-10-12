from django.db import models

# Create your models here.

class Product(models.Model):
  product = models.ProductField(upload_to='products')
  product_name =  models.CharField(max_length=200)
  product_desc = models.TextField()

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
