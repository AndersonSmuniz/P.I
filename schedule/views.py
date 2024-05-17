from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from booking.models import Booking
from service.models import Service
from .models import Schedule
from .serializer import ScheduleSerializer
from datetime import datetime, timedelta, timezone
from rest_framework.views import APIView


def get_available_slots(day):
    # Obtenha todos os horários disponíveis para o dia especificado
    available_schedules = Schedule.objects.filter(day=day)

    # Divida os horários disponíveis em intervalos de uma hora
    available_slots = []
    start_time = datetime.combine(
        datetime.now().date(), datetime.min.time()
    )  # Horário inicial no dia atual
    end_time = start_time + timedelta(hours=1)  # Próxima hora
    for schedule in available_schedules:
        while start_time < schedule.start:
            available_slots.append({"start": start_time, "end": end_time})
            start_time += timedelta(hours=1)
            end_time += timedelta(hours=1)

        start_time = max(start_time, schedule.end)

    # Adicione os horários disponíveis após o último horário de agendamento
    while start_time < datetime.combine(datetime.now().date(), datetime.max.time()):
        available_slots.append(
            {"start": start_time, "end": start_time + timedelta(hours=1)}
        )
        start_time += timedelta(hours=1)

    return available_slots


class AvailableScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class AvailableSlotsView(APIView):
    def get(self, request, barber, date):
        # Converte a data para o formato de Django
        data_formatada = datetime.strptime(date, "%Y-%m-%d").date()
        # Calcula o dia da semana equivalente à data fornecida
        dia_semana = data_formatada.isoweekday() + 1
        if dia_semana == 8:
            dia_semana = 1
        print(dia_semana, request)
        # Obtém o horário de trabalho do barbeiro no dia da semana fornecido
        schedule = Schedule.objects.filter(
            collaborator_user=barber, day=dia_semana
        ).first()
        print(schedule)
        if not schedule:
            print("aqui")
            return Response(
                {
                    "message": "Barbeiro não possui horário disponível para o dia selecionado"
                },
                status=400,
            )

        print("book")
        # Obtém os agendamentos para o dia fornecido
        data_formatada_datetime = datetime.combine(data_formatada, datetime.min.time())
        # Filtrando os bookings com base na data de agendamento e no horário de início
        bookings = Booking.objects.filter(
            date_shedule=schedule, start_booking=data_formatada_datetime
        )

        print(bookings)
        # Obtém os serviços escolhidos pelo cliente
        services_ids = request.GET.getlist("services[]")
        print(services_ids)
        services = Service.objects.filter(id__in=services_ids)
        print("qqqqqq", services)

        # Calcula a duração total dos serviços escolhidos
        total_duration = sum([service.duration for service in services])
        print(total_duration)

        # Calcula o horário final do barbeiro
        horario_final = schedule.end
        print("22222222", horario_final)
        # Calcula quantos horários livres estão disponíveis
        horarios_livres = []
        horario_atual = schedule.start
        print(horario_atual < horario_final)
        while horario_atual < horario_final:
            horario_disponivel = True

            for booking in bookings:
                booking_start = datetime.combine(data_formatada, booking.start_booking)
                booking_end = booking_start + timedelta(minutes=booking.time_required)

                if booking_start <= horario_atual < booking_end:
                    horario_disponivel = False
                    break

            if horario_disponivel:
                horarios_livres.append(horario_atual.strftime("%H:%M"))

            horario_atual += timedelta(minutes=total_duration)
        print("aaaaaaa", horarios_livres)
        return Response({"id": schedule.id, "horarios_livres": horarios_livres})
