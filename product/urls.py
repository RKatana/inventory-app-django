from django.urls import path
from .views import CreateProductView, ProductListView, ProductByIdView, ProductByStoreIdView


urlpatterns = [
    path('createproduct/', CreateProductView.as_view(), name='createproduct'),
    path('products/', ProductListView.as_view(), name='products'),
    path('singleproduct/<pk>', ProductByIdView.as_view(), name='singleproduct'),
    path('productbystoreid/<pk>', ProductByStoreIdView.as_view(), name='product_by_store_id'),
]
