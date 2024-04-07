from rest_framework import serializers
from .models import CollaboratorUser, SalonCollaborator
from salon.serializer import SalonSerializer


class CollaboratorUserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="auth.username")
    salon_collaborators = SalonSerializer(many=True, read_only=True)

    class Meta:
        model = CollaboratorUser
        fields = [
            "auth",
            "full_name",
            "username",
            "email",
            "is_barber",
            "is_manager",
            "is_owner",
            "salon_collaborators",
            "cpf",
            "birth_date",
            "phone",
            "photo",
        ]


class SalonCollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonCollaborator
        fields = ["id", "salon", "collaborator", "status"]
