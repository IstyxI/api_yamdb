from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Создание объекта класса User."""

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        """Запрещает использовать повторно username и email."""

        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует'
            )
        return data


class UserRecieveTokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена JWT."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
