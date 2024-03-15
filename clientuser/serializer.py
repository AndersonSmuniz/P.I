from rest_framework import serializers
from clientuser.models import ClientUser


class ClientUserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="auth.username")

    class Meta:
        model = ClientUser
        fields = [
            "auth",
            "full_name",
            "username",
            "email",
            "cpf",
            "birth_date",
            "phone",
            "photo",
        ]
