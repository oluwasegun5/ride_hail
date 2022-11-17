from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from main_app.models import User


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
