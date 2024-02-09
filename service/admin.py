from django.contrib import admin
from .models import Service
from collaborator_user.models import CollaboratorUser


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "salon",
        "display_collaborator",
    )
    search_fields = ("salon", "title")
    list_display_links = ("title",)
    

    def display_collaborator(self, obj):
        return ", ".join([collaborator.full_name for collaborator in CollaboratorUser.objects.all()])

    display_collaborator.short_description = "Collaborator"