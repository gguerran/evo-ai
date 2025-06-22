from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.tool import Tool
from evo_django_proj.api.serializers import (
    ToolCreateSerializer,
    ToolListSerializer,
    ToolDetailSerializer,
    ToolUpdateSerializer,
)


class ToolViewSet(BaseModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolListSerializer
    permission_classes = [IsAuthenticated]
    model = Tool
    action_serializer_classes = {
        "list": ToolListSerializer,
        "retrieve": ToolDetailSerializer,
        "create": ToolCreateSerializer,
        "update": ToolUpdateSerializer,
        "partial_update": ToolUpdateSerializer,
    }
