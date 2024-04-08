from rest_framework import serializers
from .models import Service, ClientService, CollaboratorService
from collaborator_user.serializer import CollaboratorUserSerializer
from collaborator_user.models import CollaboratorUser


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "salon",
            "title",
            "price",
            "image",
            "description",
            "status",
            "duration",
            "recurrence",
            "commission",
        ]


class ClientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientService
        fields = ["client_user", "services", "status"]


class CollaboratorServiceSerializer(serializers.ModelSerializer):

    collaborator_details = CollaboratorUserSerializer(
        source="collaborator_user", read_only=True
    )

    class Meta:
        model = CollaboratorService
        fields = "__all__"
