from django.contrib.auth import get_user_model,logout,login
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import update_last_login
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.schemas import AutoSchema
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import LoginUserSerializer, MerchantSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny,IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view
import coreapi
from .models import User
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        # override view introspection here...
        pass

# @api_view(['GET', 'POST'])
# @schema(CustomAutoSchema())
# def register(request):
    
#     """
#     List all code users, or create a new users.
#     """
#     if request.method == 'GET':
#         users = get_user_model().objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def login_user(request):
    data = {}
    reqBody = JsonResponse.loads(request.body)
    email1 = reqBody['Email_Address']
    print(email1)
    password = reqBody['password']
    try:
        Account = get_user_model().objects.get(Email_Address=email1)
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})

    token = Token.objects.get_or_create(user=Account)[0].key
    print(token)
    if not check_password(password, Account.password):
        raise ValidationError({"message": "Incorrect Login credentials"})
    if Account:
        if Account.is_active:
            print(request.user)
            login(request, Account)
            data["message"] = "user logged in"
            data["email_address"] = Account.email
            Res = {"data": data, "token": token}
            return Response(Res)
        else:
            raise ValidationError({"400": f'Account not active'})
    else:
        raise ValidationError({"400": f'Account doesnt exist'})


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class =  MyTokenObtainPairSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return  Response(serializer.data)

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class UserDetail(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request,*args,**kwargs)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all().order_by('-name')
#     serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class UserLoginAPIView(APIView):
    queryset = get_user_model().objects.all()
    serializer_classes = LoginUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({"status":status.HTTP_200_OK,"Token":token.key})


# class MerchantRegisterAPIView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = MerchantSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=request.user, status=User.merchant)
#         return Response(status=status.HTTP_201_CREATED)


class MerchantRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MerchantSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status=User.merchant)
