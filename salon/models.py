from django.db import models


class Salon(models.Model):
    """
    Modelo de salão
    """

    name_salon = models.CharField(max_length=255, unique=True, null=False)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name_salon


class Location(models.Model):
    """
    Modelo para guardar a localização do salão
    """

    type = models.CharField(max_length=20)
    coordinates = models.CharField(max_length=255)
    salon_id = models.ForeignKey(
        Salon, on_delete=models.CASCADE, related_name="salon_location"
    )

    def __str__(self):
        return "%s, %s" % (self.salon_id.name_salon, self.coordinates)
