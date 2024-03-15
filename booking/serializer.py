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
        fields = ["id", "salon", "collaborator", "client", "services", "date_shedule", "start_booking","end_booking", "status", "time_required"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["services"] = ServiceSerializer(instance.services.all(), many=True).data 
        return data

    def validate(self, data):
            # Verificar a disponibilidade da data e hora
            date_schedule = data["date_shedule"]
            start_booking = data.get("start_booking")
            end_booking = data.get("end_booking")
            
           
            # Calcular o horário de término com base no horário de início e na duração dos serviços
            if start_booking:
                total_duration = sum(service.duration for service in data["services"])
                end_booking = start_booking + timezone.timedelta(minutes=total_duration)
                data["end_booking"] = end_booking.strftime('%H:%M')
            else:
                raise serializers.ValidationError("O horário de início é obrigatório")
            
            # Verificar se o horário de início está disponível no date_schedule
            if start_booking and end_booking:
                conflicting_bookings = Booking.objects.filter(date_shedule=date_schedule, start_booking__lt=end_booking, end_booking__gt=start_booking)
                if conflicting_bookings.exists():
                    raise serializers.ValidationError("Já existe um agendamento para este horário")


            return data


