from django.urls import path
from .views import InductorListCreateView, InductorDetailView
from .views import ActivityCenterListCreateView, ActivityCenterDetailView
from .views import CostElementListCreateView, CostElementDetailView
from .views import DirectLaborListCreateView, DirectLaborDetailView
from .views import DirectRawMaterialListCreateView, DirectRawMaterialDetailView
from .views import DirectServiceListCreateView, DirectServiceDetailView
from .views import ActivityListCreateView, ActivityDetailView
from .views import ActivityCostElementListCreateView, ActivityCostElementDetailView

urlpatterns = [
    path('inductors/', InductorListCreateView.as_view(), name='inductor-list-create'),#GET y POST
    path('inductors/<int:pk>/', InductorDetailView.as_view(), name='inductor-detail'),#GET, PUT, PATCH Y DELETE

    path('activities/', ActivityCenterListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityCenterDetailView.as_view(), name='activity-detail'),
    path('cost-elements/', CostElementListCreateView.as_view(), name='cost-element-list-create'),
    path('cost-elements/<int:pk>/', CostElementDetailView.as_view(), name='cost-element-detail'),
    path('direct-labors/', DirectLaborListCreateView.as_view(), name='direct-labor-list-create'),
    path('direct-labors/<int:pk>/', DirectLaborDetailView.as_view(), name='direct-labor-detail'),
    path('direct-raw-materials/', DirectRawMaterialListCreateView.as_view(), name='direct-raw-material-list-create'),
    path('direct-raw-materials/<int:pk>/', DirectRawMaterialDetailView.as_view(), name='direct-raw-material-detail'),
    path('direct-services/', DirectServiceListCreateView.as_view(), name='direct-service-list-create'),
    path('direct-services/<int:pk>/', DirectServiceDetailView.as_view(), name='direct-service-detail'),
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('activity-cost-elements/', ActivityCostElementListCreateView.as_view(), name='activity-cost-element-list-create'),
    path('activity-cost-elements/<int:pk>/', ActivityCostElementDetailView.as_view(), name='activity-cost-element-detail'),
]
