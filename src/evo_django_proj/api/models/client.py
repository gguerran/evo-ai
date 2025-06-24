from django.db import models
from evo_django_proj.core.models.base import BaseModel


class Client(BaseModel):
    name = models.CharField("Nome", max_length=255)
    email = models.EmailField("E-mail", unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
