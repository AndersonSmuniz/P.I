# utils.py
from datetime import datetime, timedelta
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

def get_bookings(schedule:object, date:datetime)->list:
    return Booking.objects.filter(date_shedule=schedule, start_booking=date)

def get_services(service_ids:list)->list:
    return Service.objects.filter(id__in=service_ids)

def calculate_total_duration(services:list)->int:
    return sum(service.duration for service in services)

def is_slot_available(current_time:datetime, bookings:object, date:str, total_duration:int)->bool:
    for booking in bookings:
        booking_start = datetime.combine(date, booking.start_booking)
        booking_end = booking_start + timedelta(minutes=booking.time_required)
        if booking_start <= current_time < booking_end:
            return False
    return True

def get_available_slots(schedule:object, bookings:list, date:datetime, total_duration:int)->list:
    horario_final = schedule.end
    horario_atual = schedule.start
    horarios_livres = []

    while horario_atual < horario_final:
        if is_slot_available(horario_atual, bookings, date, total_duration):
            horarios_livres.append(horario_atual.strftime("%H:%M"))
        horario_atual += timedelta(minutes=total_duration)
    
    return horarios_livres
