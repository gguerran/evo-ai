from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.session import Session
from evo_django_proj.api.serializers import (
    SessionCreateSerializer,
    SessionListSerializer,
    SessionDetailSerializer,
    SessionUpdateSerializer,
)


class SessionViewSet(BaseModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionListSerializer
    permission_classes = [IsAuthenticated]
    model = Session
    action_serializer_classes = {
        "list": SessionListSerializer,
        "retrieve": SessionDetailSerializer,
        "create": SessionCreateSerializer,
        "update": SessionUpdateSerializer,
        "partial_update": SessionUpdateSerializer,
    }
