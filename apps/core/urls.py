from .views import base_page
from django.urls import path


# naming app
app_name = 'core'
urlpatterns = [
    path('', base_page, name='base')
]
