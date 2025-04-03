from django.contrib import admin
from django.urls import path, include
from autocomplete import urls as autocomplete_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the auth URLs
    path('user/', include('apps.sbc_user.urls')),  # Include the auth 
    path('', include('django_sso.sso_gateway.urls')),
    path('core/', include('apps.core.urls')),
    path("ac/", autocomplete_urls),
]