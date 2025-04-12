from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView 

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('api/auth/', include('accounts.urls')),
    
    # File Management URLs
    path('api/', include('files.urls')),
    
    # API Schema and Documentation
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Added Redoc view
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # OpenAPI schema
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
