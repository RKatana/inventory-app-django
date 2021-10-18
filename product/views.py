from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import SerializerProduct
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
      
    serializer_class = SerializerProduct()
