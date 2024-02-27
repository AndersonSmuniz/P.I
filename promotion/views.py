
from django.shortcuts import render
from rest_framework import generics
from .models import Promotion
from .serializer import PromotionSerializer
from rest_framework import viewsets

class PromotionListAPIView(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionDetailAPIView(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
