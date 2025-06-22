from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.agent_folder import AgentFolder


class AgentFolderAdmin(ModelAdmin):
    list_display = ("name", "client")
