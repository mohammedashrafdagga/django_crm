from .views import (
    client_add, client_list, client_detail, client_edit, client_delete
)
from django.urls import path


app_name = 'client'
urlpatterns = [
    path('', client_list, name='list'),
    path('add/', client_add, name='add'),
    path('<int:pk>/detail/', client_detail, name='detail'),
    path('<int:pk>/edit/', client_edit, name='edit'),
    path('<int:pk>/delete/', client_delete, name='delete'),
]
