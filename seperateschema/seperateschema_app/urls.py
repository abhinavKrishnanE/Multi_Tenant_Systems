from django.urls import path

from .views import TenantRegisterView, CreateProjectView


urlpatterns = [
    path('tenantregister/', TenantRegisterView.as_view()),
    path('createproject/', CreateProjectView.as_view()),
]