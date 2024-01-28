from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "is_collaborator", "is_client")
    list_display_links = ("full_name",)
    search_fields = ("full_name",)
