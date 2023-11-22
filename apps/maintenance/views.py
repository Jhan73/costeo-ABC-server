from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Inductor
from .serializers import InductorSerializer
from .models import ActivityCenter
from .serializers import ActivityCenterSerializer
from .models import CostElement
from .serializers import CostElementSerializer
from .models import DirectLabor
from .serializers import DirectLaborSerializer
from .models import DirectRawMaterial
from .serializers import DirectRawMaterialSerializer
from .models import DirectService
from .serializers import DirectServiceSerializer
from .models import Activity
from .serializers import ActivitySerializer
from .models import ActivityCostElement
from .serializers import ActivityCostElementSerializer

class InductorListCreateView(generics.ListCreateAPIView):#GET y POST.  para obtener la lista y crear nuevos
    queryset = Inductor.objects.all()
    serializer_class = InductorSerializer

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user.username)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        
        response_data = {
            'data': serializer.data,
            'message': 'Inductor creado exitosamente',
            'success': status.HTTP_201_CREATED
        }
        print("RESPUESTA: ",response_data)
        
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class InductorDetailView(generics.RetrieveUpdateDestroyAPIView):#GET, PUT, PATCH y DELETE para operaciones detalladas en instancias individuales del modelo
    queryset = Inductor.objects.all()
    serializer_class = InductorSerializer

#---------------- ActivityCenter --------------------
class ActivityCenterListCreateView(generics.ListCreateAPIView):
    queryset = ActivityCenter.objects.all()
    serializer_class = ActivityCenterSerializer
    
class ActivityCenterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityCenter.objects.all()
    serializer_class = ActivityCenterSerializer

#---------------  CostElement  --------------------

class CostElementListCreateView(generics.ListCreateAPIView):
    queryset = CostElement.objects.all()
    serializer_class = CostElementSerializer
    
class CostElementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostElement.objects.all()
    serializer_class = CostElementSerializer

#---------------  DirectLabor  --------------------

class DirectLaborListCreateView(generics.ListCreateAPIView):
    queryset = DirectLabor.objects.all()
    serializer_class = DirectLaborSerializer
    
class DirectLaborDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectLabor.objects.all()
    serializer_class = DirectLaborSerializer


#---------------  DirectRawMaterial  --------------------

class DirectRawMaterialListCreateView(generics.ListCreateAPIView):
    queryset = DirectRawMaterial.objects.all()
    serializer_class = DirectRawMaterialSerializer
    
class DirectRawMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectRawMaterial.objects.all()
    serializer_class = DirectRawMaterialSerializer

#---------------  DirectService  --------------------
class DirectServiceListCreateView(generics.ListCreateAPIView):
    queryset = DirectService.objects.all()
    serializer_class = DirectServiceSerializer
    
class DirectServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectService.objects.all()
    serializer_class = DirectServiceSerializer


#---------------  Activity  --------------------
class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


#---------------  ActivityCostElement  --------------------
class ActivityCostElementListCreateView(generics.ListCreateAPIView):
    queryset = ActivityCostElement.objects.all()
    serializer_class = ActivityCostElementSerializer
    
class ActivityCostElementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityCostElement.objects.all()
    serializer_class = ActivityCostElementSerializer