from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import Tenant, Project
from .tasks import create_tenant_database, add_tenant_database, run_migrations
from .serializer import ProjectSerializer


class TenantRegisterView(APIView):

    def post(self, request):
        name = request.data.get("name")
        db_name = name

        Tenant.objects.create(name=name, db_name=db_name)

        create_tenant_database(db_name)
        add_tenant_database(db_name)
        run_migrations(db_name)

        return HttpResponse({"Tenant Created Successfully"})
    

class CreateProjectView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer