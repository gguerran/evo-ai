from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.models.client import Client


class ApiKey(BaseModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="api_keys",
        verbose_name="Cliente",
    )
    name = models.CharField("Nome", max_length=255)
    provider = models.CharField("Provedor", max_length=255)
    encrypted_key = models.CharField("Chave Criptografada", max_length=255)
    is_active = models.BooleanField("Ativa", default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Chave de API"
        verbose_name_plural = "Chaves de API"
