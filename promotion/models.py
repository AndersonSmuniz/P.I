from django.db import models
from salon.models import Salon


class Promotion(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    start = models.DateTimeField()
    end = models.DateTimeField()
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.salon.name_salon} - {self.start}"

    class Meta:
        ordering = ["start"]
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
