from django.contrib import admin
from .models import Salon, Location


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "address")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    list_editable = ("address",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("type", "coordinates")
