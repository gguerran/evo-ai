from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.agent import Agent
from evo_django_proj.api.serializers import (
    AgentCreateSerializer,
    AgentListSerializer,
    AgentDetailSerializer,
    AgentUpdateSerializer,
)


class AgentViewSet(BaseModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentListSerializer
    permission_classes = [IsAuthenticated]
    model = Agent
    action_serializer_classes = {
        "list": AgentListSerializer,
        "retrieve": AgentDetailSerializer,
        "create": AgentCreateSerializer,
        "update": AgentUpdateSerializer,
        "partial_update": AgentUpdateSerializer,
    }
