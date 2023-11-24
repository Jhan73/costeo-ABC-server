from django.urls import path
from .views import CostObjectListCreateView, CostObjectDetailView
from .views import CostingListCreateView, CostingDetailView
from .views import DirectLaborCostObjectListCreateView, DirectLaborCostObjectDetailView
from .views import DirectRawMaterialCostObjectListCreateView, DirectRawMaterialCostObjectDetailView
from .views import DirectServiceCostObjectListCreateView, DirectServiceCostObjectDetailView
from .views import ActivityCostObjectListCreateView, ActivityCostObjectDetailView

urlpatterns = [
    path('costings/', CostingListCreateView.as_view(), name='costing-list-create'),
    path('costings/<int:pk>/', CostingDetailView.as_view(), name='costing-detail'),
    path('cost-objects/', CostObjectListCreateView.as_view(), name='cost-object-list-create'),
    path('cost-objects/<int:pk>/', CostObjectDetailView.as_view(), name='cost-object-detail'),
    path('direct-labor-cost-objects/', DirectLaborCostObjectListCreateView.as_view(), name='direct-labor-cost-object-list-create'),
    path('direct-labor-cost-objects/<int:pk>/', DirectLaborCostObjectDetailView.as_view(), name='direct-labor-cost-object-detail'),
    path('direct-raw-material-objects/', DirectRawMaterialCostObjectListCreateView.as_view(), name='direct-raw-material-object-list-create'),
    path('direct-raw-material-objects/<int:pk>/', DirectRawMaterialCostObjectDetailView.as_view(), name='direct-raw-material-object-detail'),
    path('direct-service-objects/', DirectServiceCostObjectListCreateView.as_view(), name='direct-service-object-list-create'),
    path('direct-service-objects/<int:pk>/', DirectServiceCostObjectDetailView.as_view(), name='direct-service-object-detail'),
    path('activity-cost-objects/', ActivityCostObjectListCreateView.as_view(), name='activity-cost-object-list-create'),
    path('activity-cost-objects/<int:pk>/', ActivityCostObjectDetailView.as_view(), name='activity-cost-object-detail'),
]