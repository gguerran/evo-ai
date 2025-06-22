from rest_framework.serializers import ModelSerializer
from evo_django_proj.api.models.user import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
