from django.contrib import admin
from .models import BaseUser

@admin.register(BaseUser)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
    ]
