from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "salon",
            "client",
            "collaborator",
            "service",
            "date",
            "status",
        ]
