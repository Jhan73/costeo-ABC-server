from rest_framework import serializers
from .models import CostObject
from .models import DirectLaborCostObject
from .models import DirectRawMaterialCostObject
from .models import DirectServiceCostObject
from .models import ActivityCostObject
from .models import Costing

class CostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costing
        fields = ['id', 'cost', 'description']
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']


class CostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostObject
        fields = '__all__'
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']

class DirectLaborCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectLaborCostObject
        fields = '__all__'
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']

class DirectRawMaterialCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectRawMaterialCostObject
        fields = '__all__'
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']

class DirectServiceCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectServiceCostObject
        fields = '__all__'
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']

class ActivityCostObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCostObject
        fields = '__all__'
        #exclude = ['created_at', 'created_user', 'updated_at', 'updated_user']


