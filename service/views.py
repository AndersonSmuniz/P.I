from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from .serializer import ServiceSerializer
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

class SalonServicesView(ListCreateAPIView):
    queryset = Service.objects.all()  # Define o queryset para todos os serviços
    serializer_class = ServiceSerializer  # Define o serializer a ser usado

    def get_queryset(self):
        # Filtra o queryset para retornar apenas os serviços relacionados ao salão específico
        salon_id = self.kwargs.get('id')
        return self.queryset.filter(salon_id=salon_id)

    def perform_create(self, serializer):
        # Define o salão associado ao serviço antes de salvar
        salon_id = self.kwargs.get('salon_id')
        serializer.save(salon_id=salon_id)
