from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Salon, Location, Favorite
from clientuser.models import ClientUser
from .serializer import LocationSerializer, SalonFavoriteSerializer, SalonSerializer, FavoriteSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action

class SalonViewSet(viewsets.ModelViewSet):
    """
    Exibir todos os salões disponiveis
    """

    queryset = Salon.objects.all()
    serializer_class = SalonFavoriteSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        print(self.request.user)
        context['user'] = self.request.user
        return context


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra favoritos pelo usuário autenticado
        return Favorite.objects.filter(client_user=self.request.user.pk)

    def create(self, request, *args, **kwargs):
        salon_id = request.data.get('salon')
        salon = Salon.objects.get(id=salon_id)
        client_user = ClientUser.objects.get(pk=request.user)
        favorite, created = Favorite.objects.get_or_create(client_user=client_user, salon=salon)
        
        if created:
            return Response(self.get_serializer(favorite).data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Salon already in favorites."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            favorite = Favorite.objects.get(client_user=request.user.pk, salon_id=kwargs['pk'])
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response({"detail": "Favorite not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])
    def list_favorites(self, request, *args, **kwargs):
        favorites = self.get_queryset()
        serializer = SalonSerializer(favorites, many=True)
        return Response(serializer.data)
