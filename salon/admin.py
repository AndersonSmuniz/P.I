from django.contrib import admin
from .models import Salon, Location


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ("id", "name_salon", "address")
    search_fields = ("name_salon",)
    list_display_links = ("id",)
    list_editable = (
        "name_salon",
        "address",
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("salon_id", "type", "coordinates")
    search_fields = ("salon_id",)
