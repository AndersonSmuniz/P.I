from django.contrib.auth.models import AbstractUser


class Auth(AbstractUser):
    """
    Model de autenticação
    """

    pass

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
