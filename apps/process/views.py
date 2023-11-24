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
from .models import Costing
from .serializers import CostingSerializer

# ----------------- Costing -----------------------

class CostingListCreateView(generics.ListCreateAPIView):
    queryset = Costing.objects.all()
    serializer_class = CostingSerializer
    
class CostingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Costing.objects.all()
    serializer_class = CostingSerializer

# ----------------- Cost Object -----------------------
class CostObjectListCreateView(generics.ListCreateAPIView):
    queryset = CostObject.objects.all()
    serializer_class = CostObjectSerializer

    def create(self, request, *args, **kwargs):
        cost_objects_data = request.data.get('cost_objects', [])
        serializer = self.get_serializer(data=cost_objects_data, many=True)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        response_data = {
            'data': serializer.data,
            'message': 'Lista de Objetos de costo creada exitosamente',
            'success': status.HTTP_201_CREATED
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


    
class CostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostObject.objects.all()
    serializer_class = CostObjectSerializer

# ----------------- Direct Labor -----------------------
class DirectLaborCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectLaborCostObject.objects.all()
    serializer_class = DirectLaborCostObjectSerializer
    
class DirectLaborCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectLaborCostObject.objects.all()
    serializer_class = DirectLaborCostObjectSerializer

# ----------------- Direct Raw Material -----------------------
class DirectRawMaterialCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectRawMaterialCostObject.objects.all()
    serializer_class = DirectRawMaterialCostObjectSerializer
    
class DirectRawMaterialCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectRawMaterialCostObject.objects.all()
    serializer_class = DirectRawMaterialCostObjectSerializer

# ----------------- Direct Service -----------------------
class DirectServiceCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = DirectServiceCostObject.objects.all()
    serializer_class = DirectServiceCostObjectSerializer
    
class DirectServiceCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectServiceCostObject.objects.all()
    serializer_class = DirectServiceCostObjectSerializer

# ----------------- Activity - Cost Object -----------------------
class ActivityCostObjectListCreateView(generics.ListCreateAPIView):
    queryset = ActivityCostObject.objects.all()
    serializer_class = ActivityCostObjectSerializer
    
class ActivityCostObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityCostObject.objects.all()
    serializer_class = ActivityCostObjectSerializer