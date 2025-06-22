from django.db import models


class Session(models.Model):
    id = models.CharField("ID", primary_key=True, max_length=255)
    app_name = models.CharField("Aplicação", max_length=255)
    user_id = models.CharField("Usuário", max_length=255)
    state = models.JSONField("Estado")
    create_time = models.DateTimeField("Criado em")
    update_time = models.DateTimeField("Atualizado em")

    class Meta:
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"
