from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.models.client import Client
from evo_django_proj.api.models.agent_folder import AgentFolder
from evo_django_proj.api.choices import AgentType


class Agent(BaseModel):

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="agents", verbose_name="Cliente"
    )
    name = models.CharField("Nome", max_length=255)
    role = models.CharField("Função", max_length=255, blank=True, null=True)
    goal = models.TextField("Objetivo", blank=True, null=True)
    description = models.TextField("Descrição", blank=True, null=True)
    type = models.CharField("Tipo", max_length=20, choices=AgentType.choices)
    model = models.CharField("Modelo", max_length=255, blank=True, default="")
    instruction = models.TextField("Instruções", blank=True)
    folder = models.ForeignKey(
        AgentFolder,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agents",
        verbose_name="Pasta",
    )
    config = models.JSONField("Configuração", default=dict)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"
