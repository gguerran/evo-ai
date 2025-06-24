from django.db import models
from evo_django_proj.core.models.base import BaseModel


class Tool(BaseModel):
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)
    config_json = models.JSONField("Configuração", default=dict)
    environments = models.JSONField("Ambientes", default=dict)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Ferramenta"
        verbose_name_plural = "Ferramentas"
