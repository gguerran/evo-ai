from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.user import User


class UserAdmin(ModelAdmin):
    list_display = ("email", "is_active")
