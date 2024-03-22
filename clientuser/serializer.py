from rest_framework import serializers
from .models import ClientUser
from my_auth.models import Auth


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = [
            "username",
            "password",
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }


class ClientUserSerializer(serializers.ModelSerializer):
    auth = AuthSerializer()

    class Meta:
        model = ClientUser
        fields = [
            "auth",
            "full_name",
            "email",
            "cpf",
            "birth_date",
            "phone",
            "photo",
        ]


    def create(self, validated_data):
        auth_data = validated_data.pop("auth")
        password = auth_data.pop("password")
        auth_instance = Auth.objects.create_user(**auth_data, password=password)
        client_user_instance = ClientUser.objects.create(
            auth=auth_instance, **validated_data
        )
        return client_user_instance
