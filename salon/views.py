from rest_framework import viewsets
from .models import Salon, Location
from .serializer import LocationSerializer, SalonSerializer


class SalonViewSet(viewsets.ModelViewSet):
    """
    Exibir todos os salões disponiveis
    """

    queryset = Salon.objects.all()
    serializer_class = SalonSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
