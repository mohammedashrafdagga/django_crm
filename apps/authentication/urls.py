from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user


app_name = 'authentication'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
