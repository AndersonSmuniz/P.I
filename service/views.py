from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from .serializer import ServiceSerializer
from .models import Service, ClientService, CollaboratorService
from .serializer import (
    ServiceSerializer,
    ClientServiceSerializer,
    CollaboratorServiceSerializer
)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ClientServiceViewSet(viewsets.ModelViewSet):
    queryset = ClientService.objects.all()
    serializer_class = ClientServiceSerializer


class SalonServicesView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):

        salon_id = self.kwargs.get("id")
        return self.queryset.filter(salon_id=salon_id)

    def perform_create(self, serializer):

        salon_id = self.kwargs.get("salon_id")
        serializer.save(salon_id=salon_id)


class ServiceCollaboratorsListView(ListCreateAPIView):
    queryset = CollaboratorService.objects.all()
    serializer_class = CollaboratorServiceSerializer

    def get_queryset(self):
        service_id = self.kwargs.get("service_id")
        return CollaboratorService.objects.filter(
            service_id=service_id, status="active"
        )
