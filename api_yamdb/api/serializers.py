from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор жанра."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории."""

    class Meta:
        fields = ('name', 'slug')
        model = Category


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментария."""

    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('text', 'author', 'review', 'pub_date', 'id')
        read_only_fields = ('author', 'post', 'review')


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериализатор для произведения при 'безопасном' запросе."""

    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'name', 'year', 'description', 'genre', 'category', 'id', 'rating'
        )
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериализатор произведения."""

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category', 'id')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор отзыва на произведение."""

    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('title', 'text', 'author', 'score', 'pub_date', 'id')
        model = Review

    def validate_score(self, value):
        """Проверяет оценку на корректное значение."""
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    def validate(self, data):
        """Детальная проверка отправляемого запроса."""
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise ValidationError('Может существовать только один отзыв!')
        return data


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
