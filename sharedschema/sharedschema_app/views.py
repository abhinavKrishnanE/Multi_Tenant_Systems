from rest_framework.generics import CreateAPIView

from .serializer import TenantSerializer, ProjectSerializer
from .models import Tenant, Project


class TenantRegisterView(CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class CreateProjectView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer