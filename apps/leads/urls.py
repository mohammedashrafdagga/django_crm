from .views import lead_add, lead_list, lead_detail, lead_delete, lead_edit
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('', lead_list, name='list'),
    path('<int:pk>/detail/', lead_detail, name='detail'),
    path('<int:pk>/edit/', lead_edit, name='edit'),
    path('<int:pk>/delete/', lead_delete, name='delete'),
    path('add/', lead_add, name='add'),
]
