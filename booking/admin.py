from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salon",
        "collaborator",
        "client",
        "date",
        "commission",
        "total_amount",
        "created_at",
    )
    list_filter = ("salon", "collaborator", "client", "created_at")
    search_fields = ("salon__name", "collaborator__username", "client__username")
