from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.mcp_server import MCPServer


class MCPServerAdmin(ModelAdmin):
    list_display = ("name", "type")
