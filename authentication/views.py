from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
#from rest_framework_swagger import 



# Create your views here.
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class =  MyTokenObtainPairSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return  Response(serializer.data)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class UserDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get(self,request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)



