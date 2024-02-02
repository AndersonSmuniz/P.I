from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "collaborator_user",
        "service",
        "day",
        "start",
        "end",
        "created_date",
    )
    list_filter = ("service", "day", "start")
    search_fields = ("collaborator_user", "service__name")
    ordering = ("day", "start")
    actions = ["setar_promocao_ativa"]

    def setar_promocao_ativa(self, request, queryset):
        queryset.update(status="Ativo")

    setar_promocao_ativa.short_description = "Ativar promoções selecionadas"

    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": ("collaborator_user", "service", "day", "start", "end"),
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
    readonly_fields = "created_date"
