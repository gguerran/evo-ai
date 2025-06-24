from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.audit_log import AuditLog


class AuditLogCreateSerializer(ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"


class AuditLogListSerializer(ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"


class AuditLogDetailSerializer(ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"


class AuditLogUpdateSerializer(ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"
