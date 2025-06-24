from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.mcp_server import MCPServer
from evo_django_proj.api.serializers import (
    MCPServerCreateSerializer,
    MCPServerListSerializer,
    MCPServerDetailSerializer,
    MCPServerUpdateSerializer,
)


class MCPServerViewSet(BaseModelViewSet):
    queryset = MCPServer.objects.all()
    serializer_class = MCPServerListSerializer
    permission_classes = [IsAuthenticated]
    model = MCPServer
    action_serializer_classes = {
        "list": MCPServerListSerializer,
        "retrieve": MCPServerDetailSerializer,
        "create": MCPServerCreateSerializer,
        "update": MCPServerUpdateSerializer,
        "partial_update": MCPServerUpdateSerializer,
    }
