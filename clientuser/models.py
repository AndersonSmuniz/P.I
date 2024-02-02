from django.db import models
from core.models import ExtraField
from my_auth.models import Auth


class ClientUser(ExtraField):
    cpf = models.CharField(max_length=11, null=False, blank=False)

    auth = models.OneToOneField(
        Auth,
        on_delete=models.CASCADE,
        verbose_name="Account",
        related_name="client",
        primary_key=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Cleinte"
        verbose_name_plural = "Clientes"
