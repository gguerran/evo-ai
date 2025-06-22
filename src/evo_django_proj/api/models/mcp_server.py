from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.choices import ConfigType, MCPServerType


class MCPServer(BaseModel):

    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)
    config_type = models.CharField(
        "Tipo de Configuração",
        max_length=20,
        choices=ConfigType.choices,
        default=ConfigType.STUDIO,
    )
    config_json = models.JSONField("Configuração", default=dict)
    environments = models.JSONField("Ambientes", default=dict)
    tools = models.JSONField("Ferramentas", default=list)
    type = models.CharField(
        "Tipo",
        max_length=20,
        choices=MCPServerType.choices,
        default=MCPServerType.OFFICIAL,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Servidor MCP"
        verbose_name_plural = "Servidores MCP"
