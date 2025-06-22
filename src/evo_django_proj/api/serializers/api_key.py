from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.api_key import ApiKey


class ApiKeyCreateSerializer(ModelSerializer):
    class Meta:
        model = ApiKey
        fields = "__all__"


class ApiKeyListSerializer(ModelSerializer):
    class Meta:
        model = ApiKey
        fields = "__all__"


class ApiKeyDetailSerializer(ModelSerializer):
    class Meta:
        model = ApiKey
        fields = "__all__"


class ApiKeyUpdateSerializer(ModelSerializer):
    class Meta:
        model = ApiKey
        fields = "__all__"
