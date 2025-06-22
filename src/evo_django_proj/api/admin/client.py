from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.client import Client


class ClientAdmin(ModelAdmin):
    list_display = ("name", "email")
