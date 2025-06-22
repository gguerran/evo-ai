from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.session import Session


class SessionAdmin(ModelAdmin):
    list_display = ("id", "app_name", "user_id")
