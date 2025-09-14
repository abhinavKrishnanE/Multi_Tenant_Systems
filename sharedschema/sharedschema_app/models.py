from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name