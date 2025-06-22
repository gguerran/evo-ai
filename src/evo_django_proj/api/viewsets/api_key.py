from rest_framework.permissions import IsAuthenticated

from evo_django_proj.core.viewsets.base import BaseModelViewSet
from evo_django_proj.api.models.api_key import ApiKey
from evo_django_proj.api.serializers import (
    ApiKeyCreateSerializer,
    ApiKeyListSerializer,
    ApiKeyDetailSerializer,
    ApiKeyUpdateSerializer,
)


class ApiKeyViewSet(BaseModelViewSet):
    queryset = ApiKey.objects.all()
    serializer_class = ApiKeyListSerializer
    permission_classes = [IsAuthenticated]
    model = ApiKey
    action_serializer_classes = {
        "list": ApiKeyListSerializer,
        "retrieve": ApiKeyDetailSerializer,
        "create": ApiKeyCreateSerializer,
        "update": ApiKeyUpdateSerializer,
        "partial_update": ApiKeyUpdateSerializer,
    }
