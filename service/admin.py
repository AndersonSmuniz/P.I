from django.contrib import admin
from .models import Service, Category
from collaborator_user.models import CollaboratorUser

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "salon",
        "display_collaborator",
        "category",
    )
    search_fields = ("salon__name", "title")
    list_display_links = ("title",)

    def display_collaborator(self, obj):
        return ", ".join([collaborator.full_name for collaborator in obj.collaborator_user.all()])

    display_collaborator.short_description = "Collaborator"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    search_fields = ("title",)

