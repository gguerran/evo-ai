from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.agent_folder import AgentFolder


class AgentFolderCreateSerializer(ModelSerializer):
    class Meta:
        model = AgentFolder
        fields = "__all__"


class AgentFolderListSerializer(ModelSerializer):
    class Meta:
        model = AgentFolder
        fields = "__all__"


class AgentFolderDetailSerializer(ModelSerializer):
    class Meta:
        model = AgentFolder
        fields = "__all__"


class AgentFolderUpdateSerializer(ModelSerializer):
    class Meta:
        model = AgentFolder
        fields = "__all__"
