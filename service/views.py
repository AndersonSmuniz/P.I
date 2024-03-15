from rest_framework import viewsets
from .models import Service, ClientService
from .serializer import (
    ServiceSerializer,
    ClientServiceSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ClientServiceViewSet(viewsets.ModelViewSet):
    queryset = ClientService.objects.all()
    serializer_class = ClientServiceSerializer
