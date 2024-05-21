from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking
from service.models import Service
from .serializer import BookingSerializer
from schedule.models import Schedule


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()

        # Obter os serviços selecionados e removê-los dos dados
        services_ids = request.GET.getlist("services[]")
        services_data = mutable_data.pop("service", [])

        # Obter o ID da instância de Schedule usando o primeiro valor da lista fornecida
        schedule_id = mutable_data.pop("date_shedule", None)

        # Verificar se o ID é fornecido e obter a instância de Schedule correspondente
        schedule_instance = None
        if schedule_id is not None:
            schedule_instance = Schedule.objects.get(pk=schedule_id[0])

            print(schedule_instance)

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        # Calculando a comissão e o total_amount
        total_commission = sum(
            Service.objects.get(id=service_id).commission
            for service_id in services_data
        )
        total_amount = sum(
            Service.objects.get(id=service_id).price for service_id in services_data
        )

        # Criando a instância do Booking
        booking = Booking.objects.create(
            salon_id=mutable_data["salon"],
            collaborator_id=mutable_data["collaborator"],
            client_id=mutable_data["client"],
            date=schedule_instance.id,
            start_booking=mutable_data[
                "start_booking"
            ],  # Adicionando o horário de início
            end_booking=None,  # Inicialmente definido como None
            status=mutable_data.get("status", 1),
            total_amount=total_amount,
            commission=total_commission,
            time_required=None,  # Será calculado após salvar
        )

        # Adicionando os serviços ao Booking
        booking.service.set(services_data)

        # Calculando o tempo necessário após salvar
        total_duration = sum(service.duration for service in booking.services.all())
        booking.time_required = total_duration
        booking.save()  # Salvando novamente para atualizar o tempo necessário

        # Calculando o horário de término e salvando novamente
        booking.end_booking = booking.start_booking + total_duration
        booking.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
