from django.contrib import admin
from django.urls import path, include
from autocomplete import urls as autocomplete_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the auth URLs
    path('', include('apps.core.urls')),
    path('auth/', include('apps.sbc_auth.urls')),
    path('it/', include('apps.items.urls')),
    path('part/', include('apps.partners.urls')),
    path('com/', include('apps.commercial.urls')),
    path('acc/', include('apps.accounting.urls')),
    path('fin/', include('apps.finance.urls')),
    path("ac/", autocomplete_urls),
]