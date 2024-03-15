from django.db import models
from collaborator_user.models import CollaboratorUser
from salon.models import Salon
from clientuser.models import ClientUser
from schedule.models import Schedule
from service.models import Service


class Booking(models.Model):
    STATUS_BOOKING = [
        (1, "livre"),
        (2, "ocupado"),
        (3, "finalizado"),
        (4, "desativo"),
    ]

    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name="bookings_salon",
    )
    collaborator = models.ForeignKey(
        CollaboratorUser,
        on_delete=models.PROTECT,
        related_name="bookings_collaborator",
    )
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.PROTECT,
        related_name="bookings_client",
    )
    service = models.ManyToManyField(
        Service,
        related_name="bookings",
    )
    date = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name="bookings_schedule",
        null=True
    )
    status = models.IntegerField(
        choices=STATUS_BOOKING,
        default=1,
    )
    commission = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.client} - {self.date}"

    class Meta:
        ordering = ["-created_at"]  # Ordenar por data de criação, do mais recente para o mais antigo
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        unique_together = ["salon", "date"]  # Garantir que não haja agendamentos duplicados para um mesmo salão e data de agendamento
