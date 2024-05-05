from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finanzas/', include('apps.finanzas.urls')),
    path('rh/', include('apps.rh.urls')),
]
