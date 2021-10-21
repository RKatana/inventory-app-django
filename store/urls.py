from django.urls import path
from .views import StoreByUserIdView, StoreDetail, StoreListView


urlpatterns = [
    path('stores/', StoreListView.as_view(), name='stores'),
    # path('singlestore/<pk>',StoreByIdView.as_view(), name='singlestore'),
    # path('createstore/', CreateStoreView.as_view(), name='createstore'),
    path('storebyuserid/<pk>',StoreByUserIdView.as_view(), name='storebyuserid'),
    path('storedetail/<int:pk>/', StoreDetail.as_view(), name='store_details'),
]