from rest_framework import viewsets
from .models import ClientUser
from .serializer import ClientUserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer
