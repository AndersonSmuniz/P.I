from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "display_salon",
        "display_service",
        "day",
        "start",
        "end",
        "created_date",
    )
    list_filter = (
        "salon",
        "service",
        "day",
        "start",
    )
    search_fields = (
        "collaborator_user",
        "service",
    )
    ordering = (
        "day",
        "start",
    )
    actions = ["setar_promocao_ativa"]

    def display_salon(self, obj):
        return obj.salon.name_salon

    display_salon.short_description = "Salon"

    # def display_collaborator_user(self, obj):
    #     return obj.collaborator_user

    # display_collaborator_user.short_description = "Collaborator User"

    def display_service(self, obj):
        return ", ".join([service.title for service in obj.service.all()])

    display_service.short_description = "Service"

    def setar_promocao_ativa(self, request, queryset):
        queryset.update(status="Ativo")

    setar_promocao_ativa.short_description = "Ativar promoções selecionadas"

    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": (
                    "salon",
                    "collaborator_user",
                    "service",
                    "day",
                    "start",
                    "end",
                ),
            },
        ),
        (
            "Outras Informações",
            {
                "fields": ("created_date",),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("created_date",)
