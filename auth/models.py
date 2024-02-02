from django.db import models
from django.contrib.auth.models import AbstractUser


class Auth(AbstractUser):
    """
    Model de autenticação
    """

    pass

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
