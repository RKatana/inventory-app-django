from django.urls import path
from .views import CreateProductView, ProductListView, ProductByIdView


urlpatterns = [
    path('createproduct/', CreateProductView.as_view(), name='createproduct'),
    path('products/', ProductListView.as_view(), name='products'),
    path('singleproduct/', ProductByIdView.as_view(), name='singleproduct'),
]
