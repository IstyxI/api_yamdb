from rest_framework import serializers

from reviews.models import Title, Genre, Category, Comment


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        fields = ('name', 'year', 'description', 'genre', 'category', 'id')
        model = Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug', 'id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug', 'id')
        model = Category


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    title = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = (
            'author', 'title', 'review', 'text', 'created', 'id', 'post_id'
        )
        read_only_fields = ('author', 'post', 'review')
