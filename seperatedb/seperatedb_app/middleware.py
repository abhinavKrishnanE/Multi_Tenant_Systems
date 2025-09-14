from django.db import connections

import threading

from .models import Tenant
from .tasks import add_tenant_database


_thread_locals = threading.local()

def set_current_request(request):
    _thread_locals.request = request

def get_current_request():
    return getattr(_thread_locals, "request", None)


class TenantDBMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_current_request(request)

        host = request.get_host().split(":")[0]
        subdomain = host.split(".")[0]

        try:
            tenant = Tenant.objects.get(name=subdomain)
            request.tenant = tenant
            request.db_name = tenant.db_name
            add_tenant_database(tenant.db_name)
        except Tenant.DoesNotExist:
            request.tenant = None
            request.db_name = "default"

        response = self.get_response(request)
        return response