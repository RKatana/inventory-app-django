from rest_framework import serializers
from .models import Profile             
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Profile
from django.utils.translation import ugettext_lazy as _


#Your serializers here

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile 
    fields = ('id', 'username', 'profilePic', 'bio', 'occupation', 'phone', 'url')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'is_staff', 'is_superuser',)
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
        fields = ('name','password', 'password2', 'email',)

        def validate(self,attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            return attrs

        def create(self, validated_data):
            user = get_user_model().objects.create(name=validated_data['name'],
                                                    email=validated_data['email'],
                                                    )
            user.set_password(validated_data['password'])
            user.save()
            return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label = _("Password"),
        style = {'input_type': 'password',},
        trim_whitespace = False,
    )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile()
        fields = ('id', 'username', 'profilePic', 'bio', 'occupation', 'phone', 'url')

        fields = ('id', 'username', 'profilePic', 'bio', 'occupation', 'phone', 'url')
