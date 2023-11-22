from django.db import models
from apps.maintenance.models import DirectLabor
from apps.maintenance.models import DirectRawMaterial
from apps.maintenance.models import DirectService
from apps.maintenance.models import Activity


class CostObject (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    profit_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    sales_value = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Process_cost_objects'

    def __str__(self):
        return self.name

class DirectLaborCostObject (models.Model):
    direct_labor_id = models.ForeignKey(DirectLabor, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    class Meta:
        db_table = 'Process_direct_labor_cost_objects'

    def __str__(self):
        return self.cant

class DirectRawMaterialCostObject (models.Model):
    direct_raw_material_id = models.ForeignKey(DirectRawMaterial, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    class Meta:
        db_table = 'Process_direct_raw_material_cost_objects'

    def __str__(self):
        return self.cant

class DirectServiceCostObject (models.Model):
    direct_service_id = models.ForeignKey(DirectService, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    class Meta:
        db_table = 'Process_direct_service_cost_objects'
    
    def __str__(self):
        return self.cant

class ActivityCostObject (models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)


# class ActivityCostElement (models.Model):
#     activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
#     cost_element_id = models.ForeignKey(CostElement, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def __str__(self):
#         return self.cant
