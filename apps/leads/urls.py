from .views import add_leads
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('add/', add_leads, name='add'),
]
