from rest_framework import serializers
from .models import Booking
from service.models import Service
from service.serializer import ServiceSerializer
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)
    time_required = serializers.IntegerField(read_only=True)
    end_booking = serializers.TimeField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "salon", "collaborator", "client", "services", "date_shedule", "start_booking", "end_booking", "status", "time_required"]

    