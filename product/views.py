from .serializers import ProductSerializer,ProductListSerializer
from .models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
# Create your views here.

class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ProductListView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

    product_param = openapi.Parameter('product', in_=openapi.IN_QUERY, description='Enter any product id', type=openapi.TYPE_INTEGER)

#     @swagger_auto_schema(manual_parameters=[product_param])
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class ProductByStoreIdView(APIView):
    
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request,pk):
        product = Product.objects.filter(store__id=pk)
        serializer = self.serializer_class(product, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched product',
            'product': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
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
                'message': 'Product successfully registered',
                'product': serializer.data
            }
            return Response(response, status=status_code)


class ProductListView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(query_serializer=ProductListSerializer, responses={200: ProductSerializer(many=True)})
    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched products',
            'products': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)