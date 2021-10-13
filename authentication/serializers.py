from rest_framework import serializers
from .models import Profile             
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)
        token['email'] = user.email
        return token


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ('id', 'username', 'profile_pic', 'bio', 'occupation', 'phone', 'url')














