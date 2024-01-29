from django.db import models
from salon.models import Salon
from colaborator_user import Colaborator_user

class Service(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    colaborator_user = models.ManyToManyField(Colaborator_user, on_delete=models.CASCADE, through='Colaboratoruser_service')
    title = models.CharField(max_length=100, null=False, blank=False)