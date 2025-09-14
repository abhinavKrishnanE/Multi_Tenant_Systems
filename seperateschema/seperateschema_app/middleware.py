from django.db import connection

from .models import Tenant


class SchemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        host = request.get_host().split(":")[0]
        subdomain = host.split(".")[0]

        try:
            tenant = Tenant.objects.get(name=subdomain)
            schema = tenant.schema_name
            request.tenant = tenant
        except Tenant.DoesNotExist:
            schema = "public"
            request.tenant = None

        request.tenant_schema = schema

        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO "{schema}"')

        response = self.get_response(request)

        with connection.cursor() as cursor:
            cursor.execute('SET search_path TO public')

        return response