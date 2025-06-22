from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.mcp_server import MCPServer


class MCPServerCreateSerializer(ModelSerializer):
    class Meta:
        model = MCPServer
        fields = "__all__"


class MCPServerListSerializer(ModelSerializer):
    class Meta:
        model = MCPServer
        fields = "__all__"


class MCPServerDetailSerializer(ModelSerializer):
    class Meta:
        model = MCPServer
        fields = "__all__"


class MCPServerUpdateSerializer(ModelSerializer):
    class Meta:
        model = MCPServer
        fields = "__all__"
