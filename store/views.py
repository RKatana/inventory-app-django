from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from authentication.models import User
from .serializer import StoreListSerializer
from .models import Store
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from rest_framework.schemas import AutoSchema
from rest_framework.decorators import api_view
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


class StoreListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer

    store_param = openapi.Parameter('store', in_=openapi.IN_QUERY, description='Enter any store name', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[store_param])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
      
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

      
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




class CreateStoreupdateAPIView(APIView):
    serializer_class = StoreListSerializer
    stores = Store.objects.all()
    lookup_field = 'pk'
    permissions_classes = [IsAuthenticatedAndOwner]