from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.client import Client


class ClientCreateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientUpdateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
