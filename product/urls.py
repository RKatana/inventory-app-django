from django.urls import path
from .views import ProductDetail, ProductListView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('productdetail/<int:pk>/',
         ProductDetail.as_view(), name='product_details'),

]
