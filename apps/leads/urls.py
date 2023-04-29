from .views import lead_add, lead_list, lead_detail
from django.urls import path


app_name = 'leads'
urlpatterns = [
    path('', lead_list, name='list'),
    path('detail/<int:pk>/', lead_detail, name='detail'),
    path('add/', lead_add, name='add'),
]
