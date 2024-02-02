from django.db import models
from user.models import User

class ClientUser(models.Model):
    cpf = models.CharField(max_length=11, null=False, blank=False)

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Account", primary_key=True 
    )


    def __str__(self):
        return self.full_name
    