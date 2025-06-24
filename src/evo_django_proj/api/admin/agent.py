from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.agent import Agent


class AgentAdmin(ModelAdmin):
    list_display = ("name", "client")
