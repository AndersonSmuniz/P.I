from django.shortcuts import render
from rest_framework import generics
from .models import Schedule
from .serializer import ScheduleSerializer
from rest_framework import viewsets

class ScheduleListAPIView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
