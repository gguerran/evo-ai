from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.agent import Agent


class AgentCreateSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class AgentListSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class AgentDetailSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"


class AgentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"
