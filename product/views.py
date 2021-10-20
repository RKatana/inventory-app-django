from .serializers import ProductSerializer, ProductistSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsMerchant
# Create your views here.

class  CreateProductView(APIView):
    
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(request_body=ProductSerializer, responses={201: ProductSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Product successfully created',
                'product': serializer.data
            }
            return Response(response, status=status_code)
        
    @swagger_auto_schema(request_body=ProductSerializer, responses={201: ProductSerializer(many=True)})
    def delete(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Product successfully deleted',
                'product': serializer.data
            }
            return Response(response, status=status_code)


class ProductListView(APIView):    
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema(query_serializer=ProductistSerializer, responses={200: ProductSerializer(many=True)})
    def get(self,request):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched products',
            'products': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=ProductistSerializer, responses={200: ProductSerializer(many=True)})
    def delete(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully deleted products',
            'products': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    

class ProductByIdView(APIView):

    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(query_serializer=ProductistSerializer, responses={200: ProductSerializer(many=True)})
    def get(self, request, pk):
        product = Product.objects.filter(id=pk)
        serializer = self.serializer_class(product, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched product',
            'product': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(query_serializer=ProductistSerializer, responses={200: ProductSerializer(many=True)})
    def delete(self, request, uid):
        product = Product.objects.get(id=uid)
        serializer = self.serializer_class(product, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully deleted product',
            'product': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

