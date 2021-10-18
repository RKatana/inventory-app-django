from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['name', 'quantity', 'buying_price', 'selling_price', 'spoilt', 'payment_status', 'uid', 'store']
