from django.db import models
from evo_django_proj.core.models.base import BaseModel
from evo_django_proj.api.models.user import User


class AuditLog(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="audit_logs",
        verbose_name="Usuário",
    )
    action = models.CharField("Ação", max_length=255)
    resource_type = models.CharField("Tipo de Recurso", max_length=255)
    resource_id = models.CharField(
        "ID do Recurso", max_length=255, blank=True, null=True
    )
    details = models.JSONField("Detalhes", blank=True, null=True)
    ip_address = models.CharField("Endereço IP", max_length=255, blank=True, null=True)
    user_agent = models.CharField("User Agent", max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.action} - {self.resource_type}"

    class Meta:
        verbose_name = "Registro de Auditoria"
        verbose_name_plural = "Registros de Auditoria"
