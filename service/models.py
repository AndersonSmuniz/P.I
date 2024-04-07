from django.db import models
from salon.models import Salon
from collaborator_user.models import CollaboratorUser
from clientuser.models import ClientUser


class Service(models.Model):
    STATUS_CHOICES = [
        ("0", "Ativo"),
        ("1", "Inativo"),
    ]

    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name="services",
    )
    collaborator_user = models.ManyToManyField(
        CollaboratorUser,
        through="CollaboratorService",
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="0",
    )
    image = models.URLField(null=True,)
    duration = models.IntegerField()
    recurrence = models.IntegerField()
    description = models.TextField()
    commission = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    created_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "status"]
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"


class CollaboratorService(models.Model):
    STATUS_CHOICES = [
        ("active", "Ativo"),
        ("inactive", "Inativo"),
    ]

    collaborator_user = models.ForeignKey(
        CollaboratorUser,
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )
    created_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.collaborator_user.user.full_name} - {self.service.title}"

    class Meta:
        verbose_name = "Colaborador Serviço"
        verbose_name_plural = "Colaboradores Serviço"


class ClientService(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("confirmed", "Confirmado"),
        ("completed", "Concluído"),
        ("cancelled", "Cancelado"),
    ]

    client_user = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE,
    )
    services = models.ManyToManyField(
        Service,
        related_name="services",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )
    created_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.client_user.user.full_name} - {self.service.title}"

    class Meta:
        verbose_name = "Cliente Serviço"
        verbose_name_plural = "Clientes Serviço"
