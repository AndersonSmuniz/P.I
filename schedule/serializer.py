from rest_framework import serializers
from .models import Schedule
from booking.models import Booking  # Importe o modelo Booking aqui

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status', 'start_booking', 'end_booking'] 

class ScheduleSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ['salon', 'collaborator_user', 'day', 'start', 'end', 'bookings']
