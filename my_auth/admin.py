from django.contrib import admin
from .models import Auth


@admin.register(Auth)
class AuthAmin(admin.ModelAdmin):
    pass
