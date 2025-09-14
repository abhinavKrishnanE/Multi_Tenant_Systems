from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from django.http import HttpResponse

from .models import Tenant, Project
from .serializer import ProjectSerializer
from .tasks import create_tenant_schema


class TenantRegisterView(APIView):

    def post(self, request):
        name = request.data.get("name")
        schema_name = name

        Tenant.objects.create(name=name, schema_name=schema_name)

        create_tenant_schema(schema_name)
    
        return HttpResponse({"Tenant Created Successfully"})


class CreateProjectView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer