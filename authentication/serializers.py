from rest_framework import serializers
from .models import Profile             
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Profile, User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password


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
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('name','password', 'email',)

        def create(self, validated_data):
            passw = make_password('ghjksslley7')

            user = User(name=validated_data['name']
                        )
            # user.set_password(validated_data['password'])
            user.save()
            return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label = _("Password"),
        style = {'input_type': 'password',},
        trim_whitespace = False,
    )














