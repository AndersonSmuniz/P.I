from datetime import timezone, timedelta, datetime
from rest_framework import viewsets, status
from rest_framework.response import Response

from clientuser.models import ClientUser
from collaborator_user.models import CollaboratorUser
from salon.models import Salon
from .models import Booking
from service.models import Service
from .serializer import BookingSerializer
from schedule.models import Schedule
from schedule.utils import convert_date, get_schedule, get_weekday


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(client__auth=user)
        else:
            return Booking.objects.all()

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        print(request.data)
        salon_id = int(mutable_data["salon"])
        try:
            salon_instance = Salon.objects.get(pk=salon_id)
            print(salon_id)
        except Salon.DoesNotExist:
            return Response({"message": "Salon not found."}, status=status.HTTP_400_BAD_REQUEST)
        
        mutable_data["salon"] = salon_instance.id
        user = request.user

        services_data = mutable_data.pop("services", [])
        schedule_date_str = mutable_data.pop("date_shedule", None)
        collaborator_id = mutable_data["collaborator"]

        print(schedule_date_str, collaborator_id, 'FFFFFFFFFFFFF')

        if not schedule_date_str:
            return Response({"message": "Schedule date is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            schedule_date = convert_date(schedule_date_str)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        print("AQUI", schedule_date)
        schedule_day = get_weekday(schedule_date)
        print(schedule_day)
        schedule_instance = get_schedule(collaborator_id, schedule_day)
        print(schedule_instance)
        if not schedule_instance:
            return Response(
                {"message": "Horário de agendamento não encontrado para o colaborador e dia fornecidos."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            start_booking_str = mutable_data["start_booking"]
            start_booking_datetime = datetime.fromisoformat(start_booking_str)
            print(start_booking_datetime)
        except (KeyError, ValueError):
            return Response({"message": "Invalid start booking datetime."}, status=status.HTTP_400_BAD_REQUEST)

        mutable_data["client"] = user.id
        mutable_data["services"] = services_data
        mutable_data["date_shedule"] = schedule_instance.id
        mutable_data["start_booking"] = start_booking_datetime
        
        print(mutable_data)
        serializer = self.get_serializer(data=mutable_data)
        if not serializer.is_valid():
            print("Serializer Errors:", serializer.errors)  # Debugging statement
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print("asdaasdasdasd")
        collaborator = CollaboratorUser.objects.filter(auth=collaborator_id).first()
        client_instance = ClientUser.objects.filter(auth=user).first()

        total_commission = sum(
            Service.objects.get(id=service_id).commission
            for service_id in services_data
        )
        total_amount = sum(
            Service.objects.get(id=service_id).price for service_id in services_data
        )
        print(total_amount, total_commission)

        booking = Booking.objects.create(
            salon=salon_instance,
            collaborator=collaborator,
            client=client_instance,
            date_shedule=schedule_instance,
            start_booking=mutable_data["start_booking"],
            total_amount=total_amount,
            commission=total_commission,
        )
        print("asd")
        booking.services.set(services_data)
        total_duration = sum(service.duration for service in booking.services.all())
        booking.time_required = total_duration
        booking_end_time = booking.start_booking + timedelta(minutes=total_duration)
        booking.end_booking = booking_end_time
        booking.save()
        print("fim")
        booking_serializer = BookingSerializer(booking)
        headers = self.get_success_headers(booking_serializer.data)
        print(headers)
        return Response(
            booking_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
