from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.audit_log import AuditLog
from evo_django_proj.api.serializers import (
    AuditLogCreateSerializer,
    AuditLogListSerializer,
    AuditLogDetailSerializer,
    AuditLogUpdateSerializer,
)


class AuditLogViewSet(BaseModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogListSerializer
    permission_classes = [IsAuthenticated]
    model = AuditLog
    action_serializer_classes = {
        "list": AuditLogListSerializer,
        "retrieve": AuditLogDetailSerializer,
        "create": AuditLogCreateSerializer,
        "update": AuditLogUpdateSerializer,
        "partial_update": AuditLogUpdateSerializer,
    }
