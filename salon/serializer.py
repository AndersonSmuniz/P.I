from rest_framework import serializers
from .models import Location, Salon


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "type", "coordinates", "salon_id"]


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ["name_salon", "address"]
