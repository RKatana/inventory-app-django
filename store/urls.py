from django.urls import path
from .views import  StoreByIdView, StoreListView


urlpatterns = [
    path('stores/', StoreListView.as_view(), name='stores'),
    path('singlestore/',StoreByIdView.as_view(), name='singlestore'),
]