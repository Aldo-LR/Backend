
from .models import *
from rest_framework import serializers

class CancionSerializer(serializers.Serializer):
    class Meta:
        model = cancion
        fields = '__all__'