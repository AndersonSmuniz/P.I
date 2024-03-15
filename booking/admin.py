from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salon",
        "collaborator",
        "client",
        # "get_date_schedule_day",  # Método personalizado para acessar o campo day de date_schedule
        "commission",
        "total_amount",
        "created_at",
    )
    list_filter = ("salon", "collaborator", "client", "created_at")
    search_fields = ("salon__name", "collaborator__username", "client__username")

    def get_date_schedule_day(self, obj):
        return obj.date_schedule.day if obj.date_schedule else None  # Acessa o campo day de date_schedule
    get_date_schedule_day.short_description = "Date Schedule Day"  # Define o cabeçalho do campo no admin
