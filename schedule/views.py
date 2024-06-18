from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from booking.models import Booking
from schedule.utils import (
    calculate_total_duration,
    convert_date,
    get_weekday,
    get_available_slots,
    get_bookings,
    get_services,
    get_schedule,
)
from service.models import Service
from .models import Schedule
from .serializer import ScheduleSerializer
from datetime import datetime, timedelta, timezone
from rest_framework.views import APIView



class AvailableScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class AvailableSlotsView(APIView):
    def get(self, request, barber, date):
        print('start')
        data_formatada = convert_date(date)
        dia_semana = get_weekday(data_formatada)
        print(dia_semana)
        
        schedule = get_schedule(barber, dia_semana)
        print(schedule)
        if not schedule:
            return Response({"message": "Barbeiro não possui horário disponível para o dia selecionado"}, status=400)

        data_formatada_datetime = datetime.combine(data_formatada, datetime.min.time())
        print("data",data_formatada_datetime,data_formatada )

        bookings = get_bookings(schedule, data_formatada_datetime)
        print(bookings)

        services = get_services(request.GET.getlist("services[]"))
        print("services",services)
        if not services:
            return Response({"message": "Nenhum serviço selecionado"}, status=400)

        total_duration = calculate_total_duration(services)
        print(total_duration)

        horarios_livres = get_available_slots(schedule, bookings, total_duration)
        print(horarios_livres)

        return Response({"id": schedule.id, "horarios_livres": horarios_livres})
