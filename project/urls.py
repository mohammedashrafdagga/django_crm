
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path('auth/', include('apps.authentication.urls', namespace='authentication')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('lead/', include('apps.leads.urls', namespace='leads')),
    path('client/', include('apps.client.urls', namespace='client')),
    path("admin/", admin.site.urls),
]
