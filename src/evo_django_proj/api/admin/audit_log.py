from django.contrib.admin import ModelAdmin
from evo_django_proj.api.models.audit_log import AuditLog


class AuditLogAdmin(ModelAdmin):
    list_display = ("action", "resource_type", "user")
