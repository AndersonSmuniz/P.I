from django.contrib import admin
from .models import ClientUser


@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "cpf",
    )
    search_fields = ("cpf", "full_name",)
    list_display_links = ("full_name",)


