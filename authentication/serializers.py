from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile, User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password


#Your serializers here
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)
        
        def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

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
                'email': user.email,
                'role': user.role
            }

            return validation

        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid login credentials')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'role')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)
        token['email'] = user.email
        return token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id', 'username', 'profile_pic', 'bio', 'occupation', 'phone', 'url')














