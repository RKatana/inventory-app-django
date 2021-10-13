from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import StoreSerializer
from .models import Store
from rest_framework.decorators import action


# Create your views here.

class StoreViewSet(ReadOnlyModelViewSet):
        
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    
    
    @action(detail=False)
    def get_list(self, request):
        pass
      
    @action(detail=True)
    def get_store(self, request, pk=None):
        pass


    @action(detail=True, methods=['post', 'delete'])
    def delete_store(self, request, pk=None):
        pass