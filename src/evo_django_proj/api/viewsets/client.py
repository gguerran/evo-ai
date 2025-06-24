from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.client import Client
from evo_django_proj.api.serializers import (
    ClientCreateSerializer,
    ClientListSerializer,
    ClientDetailSerializer,
    ClientUpdateSerializer,
)


class ClientViewSet(BaseModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = [IsAuthenticated]
    model = Client
    action_serializer_classes = {
        "list": ClientListSerializer,
        "retrieve": ClientDetailSerializer,
        "create": ClientCreateSerializer,
        "update": ClientUpdateSerializer,
        "partial_update": ClientUpdateSerializer,
    }
