from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.models.client import Client


class User(BaseModel):
    email = models.EmailField("E-mail", unique=True)
    password_hash = models.CharField("Hash da Senha", max_length=128)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
        verbose_name="Cliente",
    )
    is_active = models.BooleanField("Ativo", default=False)
    is_admin = models.BooleanField("Administrador", default=False)
    email_verified = models.BooleanField("E-mail Verificado", default=False)
    verification_token = models.CharField(
        "Token de Verificação", max_length=255, null=True, blank=True
    )
    verification_token_expiry = models.DateTimeField(
        "Expiração da Verificação", null=True, blank=True
    )
    password_reset_token = models.CharField(
        "Token de Redefinição de Senha", max_length=255, null=True, blank=True
    )
    password_reset_expiry = models.DateTimeField(
        "Expiração da Redefinição de Senha", null=True, blank=True
    )

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
