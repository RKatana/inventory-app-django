from rest_framework import status
from rest_framework.views import APIView
from .serializers import ClerkLoginSerializer, UserRegistrationSerializer, UserLoginSerializer, UserListSerializer, ClerkRegistrationSerializer, StoreAdminRegistrationSerializer, UserRequestSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User



# Create your views here.
class AuthUserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


    @swagger_auto_schema(request_body=UserRegistrationSerializer, responses={201: UserRegistrationSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered',
                'user': serializer.data
            }
            return Response(response, status=status_code)


class ClerkRegistrationView(APIView):
    serializer_class = ClerkRegistrationSerializer
    permission_classes = (AllowAny,)


    @swagger_auto_schema(request_body=ClerkRegistrationSerializer, responses={201: ClerkRegistrationSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered',
                'user': serializer.data
            }
            return Response(response, status=status_code)


class StoreAdminRegistrationView(APIView):
    serializer_class = StoreAdminRegistrationSerializer
    permission_classes = (AllowAny,)


    @swagger_auto_schema(request_body=StoreAdminRegistrationSerializer, responses={201: StoreAdminRegistrationSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered',
                'user': serializer.data
            }
            return Response(response, status=status_code)


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=UserLoginSerializer, responses={200: UserLoginSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['access'],
                'authenticatedUser': {
                    'id': serializer.data['id'],
                    'name': serializer.data['name'],
                    'email': serializer.data['email'],
                    'role': serializer.data['role'],
                }
            }
            return Response(response, status=status_code)


class ClerkLoginView(APIView):
    serializer_class = ClerkLoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=ClerkLoginSerializer, responses={200: ClerkLoginSerializer(many=True)})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Merchant logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['access'],
                'authenticatedUser': {
                    'id': serializer.data['id'],
                    'name': serializer.data['name'],
                    'email': serializer.data['email'],
                    'role': serializer.data['role'],
                }
            }
            return Response(response, status=status_code)


class UserListView(APIView):
    serializer_class = UserListSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(query_serializer=UserRequestSerializer, responses={200: UserListSerializer(many=True)})
    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched users',
            'users': serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


