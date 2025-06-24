from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.api_key import ApiKey


class ApiKeyAdmin(ModelAdmin):
    list_display = ("name", "client", "provider", "is_active")
