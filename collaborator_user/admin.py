from django.contrib import admin
from .models import CollaboratorUser


class CollaboratorUserAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "is_barber",
        "is_manager",
        "display_salon_collaborators",
    ]

    def display_salon_collaborators(self, obj):
        return ", ".join([salon.name for salon in obj.salon_collaborators.all()])

    display_salon_collaborators.short_description = "Salon Collaborators"


admin.site.register(CollaboratorUser, CollaboratorUserAdmin)
