from django.db import models
from collaborator_user.models import CollaboratorUser
from salon.models import Salon


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
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    # service = models.ManyToManyField(Service, on_delete=models.CASCADE)
    collaborator_user = models.ForeignKey(CollaboratorUser, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_WEEK)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.collaborator_user.username} - {self.get_day_display()} - {self.start}"

    class Meta:
        ordering = ["day", "start"]
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        indexes = [
            models.Index(fields=["day", "start"]),
            models.Index(fields=["collaborator_user"]),
        ]
