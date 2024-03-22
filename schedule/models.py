from django.db import models
from collaborator_user.models import CollaboratorUser
from salon.models import Salon
from service.models import Service


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        (1, "Domingo"),
        (2, "Segunda"),
        (3, "Terça"),
        (4, "Quarta"),
        (5, "Quinta"),
        (6, "Sexta"),
        (7, "Sábado"),
    ]
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name="schedule_salon",
    )
    service = models.ManyToManyField(
        Service,
        related_name="schedule_service",
    )
    collaborator_user = models.ManyToManyField(
        CollaboratorUser,
        related_name="schedule_collaborator",
    )
    day = models.IntegerField(
        choices=DAYS_OF_WEEK,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.get_day_display()} - {self.start}"

    class Meta:
        ordering = ["day", "start"]
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"
