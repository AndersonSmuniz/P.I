from rest_framework import serializers
from .models import Service, ClientService, CollaboratorService


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "salon",
            "title",
            "price",
            "status",
            "duration",
            "recurrence",
            "commission",
        ]


class ClientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientService
        fields = ["client_user", "services", "status"]
