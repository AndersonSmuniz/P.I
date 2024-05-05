from django.db import models
from core.models import ExtraField
from clientuser.models import ClientUser

class Salon(ExtraField):
    """
    Modelo de salão
    """

    name_salon = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name_salon

    class Meta:
        verbose_name = "Salão"
        verbose_name_plural = "Salões"


class Location(models.Model):
    """
    Modelo para guardar a localização do salão
    """

    type = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=255)
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name="locations",
    )

    def __str__(self):
        return f"{self.salon.name_salon} - {self.coordinates}"

    class Meta:
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"

class Favorite(models.Model):
    client_user = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)