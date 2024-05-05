from rest_framework import serializers
from .models import Favorite, Location, Salon


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "type", "coordinates", "salon"]


class SalonSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Salon
        fields = ["id", "name_salon", "address", "locations", "photo"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ["id", "salon", "client_user"]

