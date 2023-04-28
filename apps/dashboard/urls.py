from .views import dashboard_page
from django.urls import path


app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_page, name='main'),
]
