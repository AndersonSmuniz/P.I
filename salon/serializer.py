from rest_framework import serializers
from .models import Location, Salon


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "type", "coordinates", "salon"]


class SalonSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Salon
        fields = ["name_salon", "address", "locations"]
