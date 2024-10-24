from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Cybrix Request API",
        default_version='v1',
        description="API documentation for portfolio",
        terms_of_service="https://www.cybrix.com/terms/",
        contact=openapi.Contact(email="contact@cybrix.com"),
        license=openapi.License(name="cybrix License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include("client_requests.urls")),
    path('api/', include("projects.urls")),
    path('api/', include("project_types.urls")),
]
