from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.agent_folder import AgentFolder
from evo_django_proj.api.serializers import (
    AgentFolderCreateSerializer,
    AgentFolderListSerializer,
    AgentFolderDetailSerializer,
    AgentFolderUpdateSerializer,
)


class AgentFolderViewSet(BaseModelViewSet):
    queryset = AgentFolder.objects.all()
    serializer_class = AgentFolderListSerializer
    permission_classes = [IsAuthenticated]
    model = AgentFolder
    action_serializer_classes = {
        "list": AgentFolderListSerializer,
        "retrieve": AgentFolderDetailSerializer,
        "create": AgentFolderCreateSerializer,
        "update": AgentFolderUpdateSerializer,
        "partial_update": AgentFolderUpdateSerializer,
    }
