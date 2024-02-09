from django.contrib import admin
from .models import ClientUser


@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "cpf",
        "auth",
    )
    search_fields = ("cpf", "full_name")
    list_display_links = ("id", "full_name")


