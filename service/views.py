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


class CategoryServicesView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("id")
        return self.queryset.filter(category_id=category_id)


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        salon_id = self.kwargs.get("id")
        return self.queryset.filter(salon_id=salon_id)


