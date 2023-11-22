from rest_framework import serializers
from .models import CostObject
from .models import DirectLaborCostObject
from .models import DirectRawMaterialCostObject
from .models import DirectServiceCostObject
from .models import ActivityCostObject

class CostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostObject
        fields = '__all__'

class DirectLaborCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectLaborCostObject
        fields = '__all__'

class DirectRawMaterialCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectRawMaterialCostObject
        fields = '__all__'

class DirectServiceCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectServiceCostObject
        fields = '__all__'

class ActivityCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCostObject
        fields = '__all__'


