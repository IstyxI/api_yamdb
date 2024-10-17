from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, ListModelMixin
)
from rest_framework.viewsets import GenericViewSet

from reviews.models import Title, Category, Genre, Comment, Review

from .serializers import (
    TitleReadSerializer,
    TitleWriteSerializer,
    CategorySerializer,
    GenreSerializer,
    CommentSerializer
)


class TitleViewSet(viewsets.ModelViewSet):
    # queryset = Title.objects.annotate(
    #     rating=Avg('reviews__score')
    # ).all()
    pagination_class = LimitOffsetPagination
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('slug', 'genre', 'name', 'year')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class CategoryViewSet(
    CreateModelMixin, ListModelMixin,
    DestroyModelMixin, GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)


class GenreViewSet(
    CreateModelMixin, ListModelMixin,
    DestroyModelMixin, GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
