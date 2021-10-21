from django.urls import path
from .views import  CreateStoreView, StoreByIdView, StoreByUserIdView, StoreListView


urlpatterns = [
    path('stores/', StoreListView.as_view(), name='stores'),
    path('singlestore/<pk>',StoreByIdView.as_view(), name='singlestore'),
    path('createstore/', CreateStoreView.as_view(), name='createstore'),
    path('storebyuserid/<pk>',StoreByUserIdView.as_view(), name='storebyuserid'),

]