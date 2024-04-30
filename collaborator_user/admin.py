from django.contrib import admin
from .models import CollaboratorUser, Curriculum


@admin.register(CollaboratorUser)
class CollaboratorUserAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "auth",
        "is_barber",
        "is_manager",
        "is_owner",
        "display_salon_collaborators",
    ]

    def display_salon_collaborators(self, obj):
        return ", ".join([str(salon) for salon in obj.salon_collaborators.all()])

    display_salon_collaborators.short_description = "Salon Collaborators"

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display=["name_course", "Type_Course"]
   

