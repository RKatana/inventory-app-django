from django.urls import path
from .views import StoreByUserIdView, StoreDetail, StoreListView


urlpatterns = [
    path('stores/', StoreListView.as_view(), name='stores'),
    path('storebyuserid/<pk>',StoreByUserIdView.as_view(), name='storebyuserid'),
    path('storedetail/<int:pk>/', StoreDetail.as_view(), name='store_details'),
]