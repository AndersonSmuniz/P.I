from django.db import models
from core.models import ExtraField
from salon.models import Salon
from my_auth.models import Auth


class SalonCollaborator(models.Model):
    collaborator = models.ForeignKey(
        "CollaboratorUser",
        on_delete=models.CASCADE,
    )

    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=255, default="ativo")

    def __str__(self):
        return (
            f"{self.collaborator.full_name} - {self.salon.name_salon} - {self.status}"
        )

    class Meta:
        verbose_name = "Colaborador do Salão"
        verbose_name_plural = "Colaboradores do Salão"


class CollaboratorUser(ExtraField):
    """
    Model do Colaborador
    """

    auth = models.OneToOneField(
        Auth,
        on_delete=models.CASCADE,
        verbose_name="Account",
        related_name="collaborator",
        primary_key=True,
    )
    is_barber = models.BooleanField(
        default=False,
    )
    is_manager = models.BooleanField(
        default=False,
    )
    is_owner = models.BooleanField(
        default=False,
    )
    salon_collaborators = models.ManyToManyField(
        Salon,
        through="SalonCollaborator",
        verbose_name="Colaborador dos Salões",
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"


class Curriculum(models.Model):
    LEVEL_COURSE = [
        (1, "Profissionalizante"),
        (2, "Técnico"),
        (3, "Superior"),
    ]
    name_course = models.CharField(max_length=30)
    course_level = models.IntegerField(choices=LEVEL_COURSE, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True)
    colaborador = models.ForeignKey(CollaboratorUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_course} - {self.institution}"
