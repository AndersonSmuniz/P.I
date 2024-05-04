from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from .serializer import ServiceSerializer
from .models import Service, Category
from .serializer import (
    ServiceSerializer,
    CategorySerializer
)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SalonServicesView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):

        salon_id = self.kwargs.get("id")
        return self.queryset.filter(salon_id=salon_id)

    def perform_create(self, serializer):

        salon_id = self.kwargs.get("salon_id")
        serializer.save(salon_id=salon_id)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


