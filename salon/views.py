from rest_framework import viewsets
from .models import Salon, Location, Favorite
from .serializer import LocationSerializer, SalonSerializer, FavoriteSerializer


class SalonViewSet(viewsets.ModelViewSet):
    """
    Exibir todos os salões disponiveis
    """

    queryset = Salon.objects.all()
    serializer_class = SalonSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer