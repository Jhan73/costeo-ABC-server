from django.db import models

class ActivityCenter (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CostElement (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    cost = models.DecimalField()
    unit_of_measure = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CostObject (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.DecimalField()
    state = models.IntegerField()
    expenses = models.DecimalField()
    profit_percentage = models.DecimalField()
    sales_value = models.DecimalField()
    igv = models.DecimalField()
    selling_price = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DirectLabor (models.Model):
    cant = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost_per_hour = models.DecimalField()
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.cant

class DirectRawMaterial (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cod = models.CharField(max_length=255)
    description = models.TextField()
    unit_cost = models.DecimalField()
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DirectService (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField()
    state = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    salary = models.DecimalField()
    hire_date = models.DateTimeField(auto_now_add=True)
    employment_status = models.CharField(max_length=255)
    hours_worked = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)
    direct_labor_id = models.ForeignKey(DirectLabor)

    def __str__(self):
        return self.name

class Group (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer)
    
    def __str__(self):
        return self.issue_date

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField()
    customer_id = models.ForeignKey(Customer)

    def __str__(self):
        return self.total

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.DateTimeField(auto_now_add=True)
    codename = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.total

class Supplier (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)
    #################Nombre Raro
    resource_id = models.ForeignKey(CostElement)
    ############################

    def __str__(self):
        return self.name

class User (models.Model):
    id = models.AutoField(primary_key=True)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
    
class Activity (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)
    activity_center_id = models.ForeignKey(ActivityCenter)

    def __str__(self):
        return self.name

class Inductor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField()
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)
    inductor_id = models.ForeignKey(Activity)

    def __str__(self):
        return self.name

class Token (models.Model):
    key = models.CharField(primary_key=True; max_length==255)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User)
    
    def __str__(self):
        return self.key





class ActivityCostElement (models.Model):
    activity_id = models.ForeignKey(Activity)
    cost_element_id = models.ForeignKey(CostElement)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.cant

class ActivityCostObject (models.Model):
    activity_id = models.ForeignKey(Activity)
    cost_object_id = models.ForeignKey(CostObject)

    def __str__(self):
        return self.cant

class CostObjectInvoice (models.Model):
    invoice_id = models.ForeignKey(Invoice)
    cost_object_id = models.ForeignKey(CostObject)
    cant = models.IntegerField()

    def __str__(self):
        return self.cant

class DirectLaborCostObject (models.Model):
    direct_labor_id = models.ForeignKey(DirectLabor)
    cost_object_id = models.ForeignKey(CostObject)
    cant = models.IntegerField()

    def __str__(self):
        return self.cant

class DirectRawMaterialCostObject1 (models.Model):
    direct_raw_material_id = models.ForeignKey(DirectRawMaterial)
    cost_object_id = models.ForeignKey(CostObject)
    cant = models.IntegerField()

    def __str__(self):
        return self.cant

class DirectsServiceCostObject (models.Model):
    direct_service_id = models.ForeignKey(DirectService)
    cost_object_id = models.ForeignKey(CostObject)
    
    def __str__(self):
        return self.cant

class GroupPermission (models.Model):
    group_id = models.ForeignKey(Group)
    permission_id = models.ForeignKey(Permission)

    def __str__(self):
        return self.cant

class SupplierDirectRawMaterial (models.Model):
    supplier_id = models.ForeignKey(Supplier)
    direct_raw_material_id = models.ForeignKey(DirectRawMaterial)

    def __str__(self):
        return self.cant

class SupplierDirectService (models.Model):
    supplier_id = models.ForeignKey(Supplier)
    direct_service_id = models.ForeignKey(DirectService)

    def __str__(self):
        return self.cant

class UserGroup (models.Model):
    user_id = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)

    def __str__(self):
        return self.cant

class UserPermission (models.Model):
    user_id = models.ForeignKey(User)
    permission_id = models.ForeignKey(Permission)

    def __str__(self):
        return self.cant