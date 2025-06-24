from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.session import Session


class SessionCreateSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SessionListSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SessionDetailSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class SessionUpdateSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
