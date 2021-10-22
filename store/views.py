from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from .serializer import StoreListSerializer, StoreSerializer
from .models import Store
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from .permissions import IsAuthenticatedAndOwner
from rest_framework import mixins
from rest_framework import generics



# # Create your views here.
class StoreDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class StoreListView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreListSerializer

#     store_param = openapi.Parameter('store', in_=openapi.IN_QUERY, description='Enter 1', type=openapi.TYPE_INTEGER)

#     @swagger_auto_schema(manual_parameters=[store_param])
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class StoreByUserIdView(APIView):
    
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(responses={200: StoreListSerializer(many=True)})
    def get(self, request,pk):
        store = Store.objects.filter(store__id=pk)
        serializer = self.serializer_class(store, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched store',
            'product': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


class StoreCreateView(APIView):
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


class StoreListView(APIView):
    serializer_class = StoreListSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(query_serializer=StoreSerializer, responses={200: StoreListSerializer(many=True)})
    def get(self, request):
        stores = Store.objects.all()
        serializer = self.serializer_class(stores, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched stores',
            'stores': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)