from django.db import models
from collaborator_user.models import CollaboratorUser
from salon.models import Salon
from clientuser.models import ClientUser
from schedule.models import Schedule
from service.models import Service
from django.utils import timezone

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
    services = models.ManyToManyField(
        Service,
        related_name="bookings",
    )
    date_shedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name="bookings_schedule",
        null=True
    )
    start_booking = models.DateTimeField()
    end_booking = models.DateTimeField(blank=True, null=True)
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
    time_required = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.client} - {self.start_booking}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
