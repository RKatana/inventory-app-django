# <<<<<<< HEAD
from rest_framework import serializers
from .models import Profile             
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password


#Your serializers here

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile 
    fields = ('id', 'username', 'profilePic', 'bio', 'occupation', 'phone', 'url')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'is_staff', 'is_superuser',)

    # def validate(self, attrs):
    #     if attrs['password'] != attrs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer,cls).get_token(user)

        token['email'] = user.email
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('password', 'password2', 'email',)

    







# >>>>>>> 15f525e866daded0189fac07fa2731298dc1d738
