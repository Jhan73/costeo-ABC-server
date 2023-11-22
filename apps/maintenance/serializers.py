from rest_framework import serializers
from .models import Inductor
from .models import ActivityCenter
from .models import CostElement
from .models import DirectLabor
from .models import DirectRawMaterial
from .models import DirectService
from .models import Activity
from .models import ActivityCostElement

class InductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inductor
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']

        
    # created_at = serializers.DateTimeField(required=False)
    # created_user = serializers.CharField(max_length=255, required=False)
    # updated_at = serializers.DateTimeField(required=False)
    # updated_user = serializers.CharField(max_length=255, required=False)

    def create(self, validated_data):
        instance = super(InductorSerializer, self).create(validated_data)
        # Puedes agregar lógica adicional aquí si es necesario
        return instance

class ActivityCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCenter
        fields = '__all__'
    
class CostElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostElement
        fields = '__all__'


class DirectLaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectLabor
        fields = '__all__'

class DirectRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectRawMaterial
        fields = '__all__'

class DirectServiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DirectService
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityCostElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCostElement
        fields = '__all__'
