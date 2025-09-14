from .middleware import get_current_request


class TenantRouter:
    
    def db_for_read(self, model, **hints):
        request = get_current_request()
        if request and hasattr(request, "db_name"):
            print(request.db_name)
            return request.db_name
        return "default"

    def db_for_write(self, model, **hints):
        request = get_current_request()
        if request and hasattr(request, "db_name"):
            print(request.db_name)
            return request.db_name
        return "default"