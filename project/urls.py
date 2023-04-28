
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path("admin/", admin.site.urls),
]
