from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "STATUS_CHOICES",
        "salon",
        "collaborator_user",
        "title",
        "status",
    )
    search_fields = ("salon", "tittle")
    list_display_links = ("id", "tittle")
    

