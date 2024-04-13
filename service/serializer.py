from rest_framework import serializers
from .models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "salon",
            "title",
            "price",
            "category",
            "image",
            "description",
            "status",
            "duration",
            "recurrence",
            "commission",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "salon",
            "description",
            "image",
        ]
