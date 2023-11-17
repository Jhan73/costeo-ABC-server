from django.urls import path
from .views import InductorListCreateView, InductorDetailView

urlpatterns = [
    path('inductors/', InductorListCreateView.as_view(), name='inductor-list-create'),
    path('inductors/<int:pk>/', InductorDetailView.as_view(), name='inductor-detail'),
]
