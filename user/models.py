from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Model de User
    """

    full_name = models.CharField(max_length=255)
    photo = models.URLField(null=True)
    is_collaborator = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
