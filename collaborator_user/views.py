from rest_framework import viewsets
from .models import CollaboratorUser, SalonCollaborator
from .serializer import CollaboratorUserSerializer, SalonCollaboratorSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = CollaboratorUser.objects.all()
    serializer_class = CollaboratorUserSerializer


class SalonCollaboratorViewSet(viewsets.ModelViewSet):
    queryset = SalonCollaborator.objects.all()
    serializer_class = SalonCollaboratorSerializer
