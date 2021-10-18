import uuid
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from authentication.models import User
from .serializer import StoreListSerializer
from .models import Store
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi



# Create your views here.

class StoreListView(APIView):
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(manual_parameters=[], responses={200: StoreListSerializer(many=True)})
    def get(self, request):
        stores = Store.object.all()
        serializer = self.serializer_class(stores, many = True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched stores',
            'stores': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


class CreateStoreView(APIView):
      
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(request_body=StoreListSerializer, responses={201: StoreListSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Store successfully created',
                'store': serializer.data
            }
            return Response(response, status=status_code)

class StoreByIdView(APIView):
        
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(manual_parameters=[], responses={200: StoreListSerializer(many=True)})
    def get(self,request,uid):
        store = Store.objects.get(id=uid)
        serializer = self.serializer_class(store, many = True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched store',
            'store': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
   