from django.db import models

from salon.models import Salon
from user.models import User


class SalonCollaborator(models.Model):
    collaborator = models.ForeignKey("CollaboratorUser", on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.collaborator.user.full_name} - {self.salon.name_salon} - {self.status}"

    class Meta:
        verbose_name = "Colaborador do Salão"
        verbose_name_plural = "Colaboradores do Salão"


class CollaboratorUser(models.Model):
    """
    Model do Colaborador
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Conta",
        primary_key=True,
    )
    is_barber = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    salon_collaborators = models.ManyToManyField(
        Salon, through="SalonCollaborator", verbose_name="Colaboradores do Salão"
    )

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"
