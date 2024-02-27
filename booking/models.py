from django.db import models
from salon.models import Salon
from collaborator_user.models import CollaboratorUser
from clientuser.models import ClientUser
from service.models import Service


class Booking(models.Model):
    """
    Model de agendamento
    """

    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name="booking",
    )
    collaborator = models.ForeignKey(
        CollaboratorUser,
        on_delete=models.PROTECT,
        related_name="booking",
    )
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.PROTECT,
        related_name="booking",
    )
    service = models.ManyToManyField(
        Service,
    )
    date = models.DateTimeField()
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

    def __str__(self) -> str:
        return f"{self.client} - {self.date}"

    class Meta:
        ordering = [
            "-date"
        ]  # Ordena as reservas pela data, da mais recente para a mais antiga
        verbose_name = "Agendamento"  # Nome singular
        verbose_name_plural = "Agendamentos"  # Nome plural
        unique_together = [
            "salon",
            "date",
        ]  # Garante que não haja agendamentos duplicados na mesma data e no mesmo salão
        permissions = [
            (
                "can_view_all_bookings",
                "Can view all bookings",
            ),  # Permissão personalizada
        ]
