from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.models.client import Client


class AgentFolder(BaseModel):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="folders", verbose_name="Cliente"
    )
    name = models.CharField("Nome", max_length=255)
    description = models.TextField("Descrição", blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Pasta de Agentes"
        verbose_name_plural = "Pastas de Agentes"
