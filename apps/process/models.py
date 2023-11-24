from django.db import models
from apps.maintenance.models import DirectLabor
from apps.maintenance.models import DirectRawMaterial
from apps.maintenance.models import DirectService
from apps.maintenance.models import Activity
from apps.maintenance.models import Inductor

class Costing(models.Model):
    id = models.AutoField(primary_key=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    state = models.IntegerField( null=True, blank=True)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profit_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sales_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    igv = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'process_costings'


class CostObject (models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(default='', max_length=20)
    quantity = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    costing_id = models.ForeignKey(Costing, on_delete=models.CASCADE)

    class Meta:
        db_table = 'process_cost_objects'

    def __str__(self):
        return self.name

class IndirectCostElement (models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    inductor = models.CharField(max_length=255)

    class Meta:
        db_table = 'process_indirect_cost_elements'
    
    def __str__(self):
        return self.quantity

class DirectLaborCostObject (models.Model):
    direct_labor_id = models.ForeignKey(DirectLabor, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'process_direct_labor_cost_objects'

    def __str__(self):
        return self.quantity

class DirectRawMaterialCostObject (models.Model):
    direct_raw_material_id = models.ForeignKey(DirectRawMaterial, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'process_direct_raw_material_cost_objects'

    def __str__(self):
        return self.quantity

class DirectServiceCostObject (models.Model):
    direct_service_id = models.ForeignKey(DirectService, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'process_direct_service_cost_objects'
    
    def __str__(self):
        return self.quantity
    
    


class ActivityCostObject (models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'process_activity_cost_objects'


# class ActivityInductor (models.Model):
#     activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
#     inductor_id = models.ForeignKey(Inductor, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'process_activity_inductors'


# class ActivityCostElement (models.Model):
#     activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
#     cost_element_id = models.ForeignKey(CostElement, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()

#     def __str__(self):
#         return self.cant
