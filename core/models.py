from django.db import models


class ExtraField(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    photo = models.URLField(null=True)

    class Meta:
        abstract = True
