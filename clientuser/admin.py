from django.contrib import admin
from .models import ClientUser


@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cpf",
        "auth",
    )
    search_fields = ("cpf",)
    list_display_links = ("id",)
    list_editable = (
        "auth",
    )


