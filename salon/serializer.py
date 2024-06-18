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


class SalonFavoriteSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Salon
        fields = ["id", "name_salon", "address", "locations", "photo", "is_favorite"]

    def get_is_favorite(self, obj):
        user = self.context['user']
        if user.is_authenticated:
            return Favorite.objects.filter(client_user=user.pk, salon=obj).exists()
        return False


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ["id", "salon", "client_user"]

