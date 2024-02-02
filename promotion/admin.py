from django.contrib import admin
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        "service",
        "salon",
        "value",
        "start",
        "end",
        "amount",
        "status",
        "created_date",
    )
    list_filter = ("service", "salon", "start", "status")
    search_fields = ("service", "salon")
    ordering = ("start",)
    actions = ["ativar_promocao", "desativar_promocao"]

    def ativar_promocao(self, request, queryset):
        queryset.update(status=True)

    ativar_promocao.short_description = "Ativar promoções selecionadas"

    def desativar_promocao(self, request, queryset):
        queryset.update(status=False)

    desativar_promocao.short_description = "Desativar promoções selecionadas"

    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": (
                    "service",
                    "salon",
                    "value",
                    "start",
                    "end",
                    "amount",
                    "status",
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
