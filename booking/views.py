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
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        salon_id = int(mutable_data["salon"])
        salon_instance = Salon.objects.get(pk=salon_id)
        mutable_data["salon"] = salon_instance
        user = request.user

        services_data = mutable_data.pop("services", [])
        schedule_date_str = mutable_data.pop("date_shedule", None)
        print(schedule_date_str)
        collaborator_id = mutable_data["collaborator"]

        if schedule_date_str:
            schedule_date = convert_date(schedule_date_str)
            schedule_day = get_weekday(schedule_date)
            schedule_instance = get_schedule(collaborator_id, schedule_day)
            print(schedule_instance)

        if not schedule_instance:
            return Response(
                {
                    "message": "Horário de agendamento não encontrado para o colaborador e dia fornecidos."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        mutable_data["client"] = user.id
        mutable_data["services"] = services_data
        mutable_data["date_shedule"] = schedule_instance.id

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        collaborator = CollaboratorUser.objects.filter(auth=collaborator_id).first()
        client_instance = ClientUser.objects.filter(auth=user).first()

        total_commission = sum(
            Service.objects.get(id=service_id).commission
            for service_id in services_data
        )
        total_amount = sum(
            Service.objects.get(id=service_id).price for service_id in services_data
        )

        booking = Booking.objects.create(
            salon=mutable_data["salon"],
            collaborator=collaborator,
            client=client_instance,
            date_shedule=schedule_instance.id,
            start_booking=mutable_data["start_booking"],
            total_amount=total_amount,
            commission=total_commission,
        )

        booking.services.set(services_data)
        total_duration = sum(service.duration for service in booking.services.all())
        booking.time_required = total_duration
        booking_date_time = datetime.combine(schedule_date, booking.start_booking)
        booking_end_time = booking_date_time + timedelta(minutes=total_duration)
        booking.end_booking = booking_end_time.time()
        booking.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
