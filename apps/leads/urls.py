from .views import leads_add, leads_list
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('', leads_list, name='list'),
    path('add/', leads_add, name='add'),
]
