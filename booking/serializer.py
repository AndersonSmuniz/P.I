from rest_framework import serializers

from clientuser.serializer import ClientUserSerializer
from collaborator_user.serializer import CollaboratorUserSerializer
from salon.serializer import SalonSerializer
from .models import Booking
from service.models import Service
from service.serializer import ServiceSerializer
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    salon = SalonSerializer(read_only=True)
    collaborator = CollaboratorUserSerializer(read_only=True)
    client = ClientUserSerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    time_required = serializers.IntegerField(read_only=True)
    end_booking = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "salon", "collaborator", "client", "services", "date_shedule", "start_booking", "end_booking", "status", "time_required", "total_amount"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['salon'] = {
            'id': instance.salon.id,
            'name': instance.salon.name_salon,
            'address': instance.salon.address,
            "photo": instance.salon.photo
        }
        representation['collaborator'] = {
            'id': instance.collaborator.pk,
            'name': instance.collaborator.full_name
        }
        representation['client'] = {
            'id': instance.client.pk,
            'name': instance.client.full_name
        }
        representation['services'] = [{
            'id': service.id,
            'title': service.title,
            'price': service.price
        } for service in instance.services.all()]
        return representation