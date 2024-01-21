from django.db import models
from django.contrib.auth.hashers import make_password


class Salon(models.Model):
    """
    Modelo de salão
    """

    name = models.CharField(max_length=255, unique=True, null=False)
    image = models.URLField(blank=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.password.startswith(("pbkdf2_sha256$", "bcrypt", "argon2")):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


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
        return "%s, %s" % (self.salon_id.name, self.coordinates)
