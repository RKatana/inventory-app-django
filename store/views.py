from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from authentication.models import User
from .serializer import StoreListSerializer,StoreSerializer
from .models import Store
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from rest_framework.schemas import AutoSchema, coreapi
from rest_framework.decorators import api_view



# Create your views here.

class StoreListView(APIView):
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)


    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def get(self, request):
        stores = Store.objects.all()
        serializer = self.serializer_class(stores, many = True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched stores',
            'stores': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def delete(self, request):
        stores = Store.objects.all()
        serializer = self.serializer_class(stores, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully deleted stores',
            'store': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def put(self, request):
        stores = Store.objects.all()
        serializer = self.serializer_class(stores, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully updated stores',
            'store': serializer.data,
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
        
    @swagger_auto_schema(request_body=StoreListSerializer, responses={201: StoreListSerializer(many=True)})
    def delete(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Store successfully deleted',
                'store': serializer.data
            }
            return Response(response, status=status_code)
    @swagger_auto_schema(request_body=StoreListSerializer, responses={201: StoreListSerializer(many=True)})
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Store successfully updated',
                'store': serializer.data
            }
            return Response(response, status=status_code)

class StoreByIdView(APIView):
        
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def get(self,request,pk):
        store = Store.objects.filter(id=pk)
        serializer = self.serializer_class(store, many = True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched store',
            'store': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def delete(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.serializer_class(store, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully deleted store',
            'store': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreSerializer(many=True)})
    def put(self, request, pk):
        store = Store.objects.get(id=pk)
        serializer = self.serializer_class(store, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully updated store',
            'store': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
   
  