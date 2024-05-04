from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import CollaboratorUser, SalonCollaborator
from .serializer import CollaboratorUserSerializer, SalonCollaboratorSerializer, BarberSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = CollaboratorUser.objects.all()
    serializer_class = CollaboratorUserSerializer


class SalonCollaboratorViewSet(viewsets.ModelViewSet):
    queryset = SalonCollaborator.objects.all()
    serializer_class = SalonCollaboratorSerializer

class CollaboratorSalonView(ListAPIView):
    queryset = CollaboratorUser.objects.all()
    serializer_class = BarberSerializer
    def get_queryset(self):
        salon_id = self.kwargs.get("id")
        queryset = CollaboratorUser.objects.filter(salon_collaborators=salon_id, is_barber=True)
        return queryset