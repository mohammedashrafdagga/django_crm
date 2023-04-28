from .views import index_page, about_page
from django.urls import path


# naming app
app_name = 'core'
urlpatterns = [
    path('', index_page, name='index'),
    path('about/', about_page, name='about')
]
