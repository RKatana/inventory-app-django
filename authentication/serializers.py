from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Clerk, Profile, StoreAdmin, User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password


#Your serializers here
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email', 'password', 'role',)
        read_only_fields = ('role',)
        
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class ClerkRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = User
        fields = ('id','name','email', 'password', 'role')
        read_only_fields = ('role',)
        
    def create(self, validated_data):
        return Clerk.objects.create_user(**validated_data)
        


class StoreAdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreAdmin
        fields = ('id','name','email', 'password', 'role',)
        read_only_fields = ('role',)
        
    def create(self, validated_data):
        return StoreAdmin.objects.create_storeadmin(**validated_data)
        
    

class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass


    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }

            return validation

        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid login credentials')


class ClerkLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass


    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }

            return validation

        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid login credentials')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'role')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id', 'username', 'profile_pic', 'bio', 'occupation', 'phone', 'url')


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role',)
