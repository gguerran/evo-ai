from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.tool import Tool


class ToolAdmin(ModelAdmin):
    list_display = ("name",)
