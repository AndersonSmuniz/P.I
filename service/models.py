from django.db import models
from salon.models import Salon
from collaborator_user import CollaboratorUser

class Service(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    collaborator_user = models.ManyToManyField(CollaboratorUser, on_delete=models.CASCADE, through='CollaboratorService')
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, null=False, blank=False)
    duration = models.IntegerField()
    recurrence = models.IntegerField()
    descriptoin = models.TextField()
    comission = models.DecimalField(max_digits=5, decimal_places=2)
    created_data = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title

class CollaboratorService(models.Model):
    collaborator_user = models.ManyToManyField(CollaboratorUser, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=False, blank=False)
    created_data = models.DateField(auto_now_add=True)