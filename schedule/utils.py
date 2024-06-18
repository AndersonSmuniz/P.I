# utils.py
from datetime import datetime, timedelta
from typing import List
from pytz import timezone
from django.utils.timezone import make_aware
from .models import Schedule
from service.models import Service
from booking.models import Booking

def convert_date(date_str:str)->datetime:
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def get_weekday(date:datetime):
    dia_semana = date.isoweekday() + 1
    return 1 if dia_semana == 8 else dia_semana

def get_schedule(barber:int, weekday:int)->object:
    return Schedule.objects.filter(collaborator_user=barber, day=weekday).first()

def get_bookings(schedule: object, date: datetime) -> list:
    print("utils",date)
    start_of_day = make_aware(datetime.combine(date.date(), datetime.min.time()))
    end_of_day = make_aware(datetime.combine(date.date(), datetime.max.time()))
    return Booking.objects.filter(date_shedule=schedule, start_booking__range=(start_of_day, end_of_day))

def get_services(service_ids:list)->list:
    return Service.objects.filter(id__in=service_ids)

def calculate_total_duration(services:list)->int:
    return sum(service.duration for service in services)

def get_booking_times(bookings: List[Booking]) -> List[datetime]:
    """
    Obtém uma lista de horários de início de cada booking, ajustados para o fuso horário local.
    """
    local_timezone = timezone('America/Sao_Paulo')  # Defina o fuso horário local
    return [booking.start_booking.astimezone(local_timezone).time() for booking in bookings]

def is_slot_available(current_time: datetime, booking_times: List[datetime]) -> bool:
    """
    Verifica se o horário atual está disponível.
    """
    local_timezone = timezone('America/Sao_Paulo')
    current_time_local = current_time.astimezone(local_timezone).time()  # Converta o horário atual para o fuso horário local
    return current_time_local not in booking_times

def get_available_slots(schedule: object, bookings: List[Booking], total_duration: int) -> List[str]:
    """
    Obtém os horários disponíveis.
    """
    booking_times = get_booking_times(bookings)
    local_timezone = timezone('America/Sao_Paulo')  # Defina o fuso horário local
    horario_final = schedule.end
    horario_atual = schedule.start.astimezone(local_timezone)  # Converta o horário inicial para o fuso horário local
    horarios_livres = []

    while horario_atual < horario_final:
        if is_slot_available(horario_atual, booking_times):
            horarios_livres.append(horario_atual.strftime("%H:%M"))
        horario_atual += timedelta(minutes=total_duration)
    
    return horarios_livres
