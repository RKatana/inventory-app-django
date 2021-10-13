from .models import Store
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ['pk', 'name', 'location','address','city','user']