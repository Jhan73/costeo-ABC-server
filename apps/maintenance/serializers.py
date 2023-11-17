from rest_framework import serializers
from .models import Inductor

class InductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inductor
        fields = '__all__'
        
    created_at = serializers.DateTimeField(required=False)
    created_user = serializers.CharField(max_length=255, required=False)
    updated_at = serializers.DateTimeField(required=False)
    updated_user = serializers.CharField(max_length=255, required=False)
