from .views import (
    lead_add, lead_list,
    lead_detail, lead_delete,
    lead_edit, convert_to_client
)
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('', lead_list, name='list'),
    path('add/', lead_add, name='add'),
    path('<int:pk>/convert-to-client/',
         convert_to_client, name='convert-to-client'),
    path('<int:pk>/detail/', lead_detail, name='detail'),
    path('<int:pk>/edit/', lead_edit, name='edit'),
    path('<int:pk>/delete/', lead_delete, name='delete'),
]
