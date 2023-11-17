from django.db import models

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
