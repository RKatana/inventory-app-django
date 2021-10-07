from django.contrib.auth import get_user_model
from rest_framework import serializers


#Your serializers here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'is_staff', 'is_superuser',)