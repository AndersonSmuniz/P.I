from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from .models import ClientUser
from my_auth.models import Auth
from .serializer import ClientUserSerializer, AuthSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import action


class ClientCreateViewSet(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer

    @action(detail=False, methods=['post', 'put'])
    def create_or_update(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = request.user
        client_user = get_object_or_404(ClientUser, pk=user)
        serializer = self.get_serializer(client_user)
        return Response(serializer.data)


class ClientUpdateViewSet(viewsets.ViewSet):
    def initialize(self, request, *args, **kwargs):
        self.client_id = kwargs['pk']

    def update(self, request, *args, **kwargs):
        client = get_object_or_404(ClientUser, id=self.client_id)
        serializer = ClientUserSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ClientDestroyViewSet(viewsets.ViewSet):
    def destroy(self, request, pk=None):
        try:
            client_user = ClientUser.objects.get(pk=pk)
        except ClientUser.DoesNotExist:
            return Response({'error': 'ClientUser não existe'}, status=status.HTTP_404_NOT_FOUND)

        client_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
