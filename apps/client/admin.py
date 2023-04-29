from django.contrib import admin
from .models import Client


# register client model to admin panel
admin.site.register(Client)
