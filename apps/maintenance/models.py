from django.db import models

class ActivityCenter (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_activity_centers'

    def __str__(self):
        return self.name
    
class Inductor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField()
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        db_table = 'maintenance_inductors'

    def __str__(self):
        return self.name

class Activity (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)
    activity_center_id = models.ForeignKey(ActivityCenter, on_delete=models.CASCADE)
    inductor_id = models.ForeignKey(Inductor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'maintenance_activities'

    def __str__(self):
        return self.name
    
    


class CostElement (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_of_measure = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_cost_elements'

    def __str__(self):
        return self.name


# class Customer (models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     telephone = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_user = models.CharField(max_length=255)
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_user = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class DirectLabor (models.Model):
    id = models.AutoField(primary_key=True)
    cant = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_direct_labors'

    def __str__(self):
        return self.cant

class DirectRawMaterial (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cod = models.CharField(max_length=255)
    description = models.TextField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_direct_raw_materials'

    def __str__(self):
        return self.name

class DirectService (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_user = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_user = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'maintenance_direct_services'

    def __str__(self):
        return self.name
    
    
class ActivityCostElement (models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    cost_element_id = models.ForeignKey(CostElement, on_delete=models.CASCADE)
    cant = models.IntegerField(default=0)

    class Meta:
        db_table = 'maintenance_activity_cost_elements'

    def __str__(self):
        return self.cant

# class Employee (models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     hire_date = models.DateTimeField(auto_now_add=True)
#     employment_status = models.CharField(max_length=255)
#     hours_worked = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_user = models.CharField(max_length=255)
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_user = models.CharField(max_length=255)
#     direct_labor_id = models.ForeignKey(DirectLabor, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Invoice(models.Model):
#     id = models.AutoField(primary_key=True)
#     issue_date = models.DateTimeField(auto_now_add=True)
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.issue_date

# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     date = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.total


# class Supplier (models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     telephone = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_user = models.CharField(max_length=255)
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_user = models.CharField(max_length=255)
#     #################Nombre Raro
#     resource_id = models.ForeignKey(CostElement, on_delete=models.CASCADE)
#     ############################

#     def __str__(self):
#         return self.name






# class CostObjectInvoice (models.Model):
#     invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     cost_object_id = models.ForeignKey(CostObject, on_delete=models.CASCADE)
#     cant = models.IntegerField()

#     def __str__(self):
#         return self.cant



# class SupplierDirectRawMaterial (models.Model):
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     direct_raw_material_id = models.ForeignKey(DirectRawMaterial, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cant

# class SupplierDirectService (models.Model):
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     direct_service_id = models.ForeignKey(DirectService, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cant


