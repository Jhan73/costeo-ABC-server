from django.db import models
    
class Activity (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_user = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name

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
    
class ActivityCostElement (models.Model):
    cantidad = models.IntegerField()

    def __str__(self):
        return self.cant

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

class CostObjectInvoice (models.Model):
    cant = models.IntegerField()

    def __str__(self):
        return self.cant

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

class DirectLaborCostObject (models.Model):
    cant = models.IntegerField()

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

class DirectRawMaterialCostObject1 (models.Model):
    cant = models.IntegerField()

    def __str__(self):
        return self.cant

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

    def __str__(self):
        return self.name

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.issue_date

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField()

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

    def __str__(self):
        return self.name

class Token (models.Model):
    key = models.CharField(primary_key=True; max_length==255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.key

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