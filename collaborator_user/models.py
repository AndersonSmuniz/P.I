from django.db import models


class CollaboratorUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birth_date = models.DateField(
        null=True,
    )
    phone = models.CharField(max_length=16)
    photo = models.URLField(blank=True)
