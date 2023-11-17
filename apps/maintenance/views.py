from django.shortcuts import render

from rest_framework import generics
from .models import Inductor
from .serializers import InductorSerializer

class InductorListCreateView(generics.ListCreateAPIView):
    queryset = Inductor.objects.all()
    serializer_class = InductorSerializer

class InductorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inductor.objects.all()
    serializer_class = InductorSerializer
