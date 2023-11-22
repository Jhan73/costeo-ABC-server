from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import CostObject
from .serializers import CostObjectSerializer
from .models import DirectLaborCostObject
from .serializers import DirectLaborCostObjectSerializer
from .models import DirectRawMaterialCostObject
from .serializers import DirectRawMaterialCostObjectSerializer
from .models import DirectServiceCostObject
from .serializers import DirectServiceCostObjectSerializer
from .models import ActivityCostObject
from .serializers import ActivityCostObjectSerializer

class CostObjectListCreateView(generics.ListCreateAPIView):
    queryset = CostObject.objects.all()
    serializer_class = CostObjectSerializer
    
class CostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostObject.objects.all()
    serializer_class = CostObjectSerializer


class DirectLaborCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectLaborCostObject.objects.all()
    serializer_class = DirectLaborCostObjectSerializer
    
class DirectLaborCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectLaborCostObject.objects.all()
    serializer_class = DirectLaborCostObjectSerializer


class DirectRawMaterialCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectRawMaterialCostObject.objects.all()
    serializer_class = DirectRawMaterialCostObjectSerializer
    
class DirectRawMaterialCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectRawMaterialCostObject.objects.all()
    serializer_class = DirectRawMaterialCostObjectSerializer


class DirectServiceCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectServiceCostObject.objects.all()
    serializer_class = DirectServiceCostObjectSerializer
    
class DirectServiceCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectServiceCostObject.objects.all()
    serializer_class = DirectServiceCostObjectSerializer


class ActivityCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = ActivityCostObject.objects.all()
    serializer_class = ActivityCostObjectSerializer
    
class ActivityCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityCostObject.objects.all()
    serializer_class = ActivityCostObjectSerializer