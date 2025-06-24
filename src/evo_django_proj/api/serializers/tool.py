from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.tool import Tool


class ToolCreateSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class ToolListSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class ToolDetailSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class ToolUpdateSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"
