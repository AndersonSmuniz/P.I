from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Schedule
from .serializer import ScheduleSerializer
from datetime import datetime, timedelta

def get_available_slots(day):
    # Obtenha todos os horários disponíveis para o dia especificado
    available_schedules = Schedule.objects.filter(day=day)

    # Divida os horários disponíveis em intervalos de uma hora
    available_slots = []
    start_time = datetime.combine(datetime.now().date(), datetime.min.time())  # Horário inicial no dia atual
    end_time = start_time + timedelta(hours=1)  # Próxima hora
    for schedule in available_schedules:
        while start_time < schedule.start:
            available_slots.append({
                'start': start_time,
                'end': end_time
            })
            start_time += timedelta(hours=1)
            end_time += timedelta(hours=1)

        start_time = max(start_time, schedule.end)

    # Adicione os horários disponíveis após o último horário de agendamento
    while start_time < datetime.combine(datetime.now().date(), datetime.max.time()):
        available_slots.append({
            'start': start_time,
            'end': start_time + timedelta(hours=1)
        })
        start_time += timedelta(hours=1)

    return available_slots

class AvailableScheduleViewSet(viewsets.ViewSet):
    serializer_class = ScheduleSerializer

    @action(detail=False, methods=['get'])
    def list_available_slots(self, request):
        # Obtenha o dia da semana atual (0 para segunda-feira, 6 para domingo)
        current_day = datetime.now().weekday() + 1

        # Obtenha os horários disponíveis para o dia atual
        available_slots = get_available_slots(current_day)

        return Response(available_slots)
