from rest_framework.serializers import ModelSerializer

from .models import Tenant, Project


class TenantSerializer(ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

    
class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'