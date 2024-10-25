from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Title, Category, Genre, Review
from api.mixins import ModelMixinSet
from api.filters import TitleFilter
from api.serializers import (
    TitleReadSerializer,
    TitleWriteSerializer,
    CategorySerializer,
    GenreSerializer,
    CommentSerializer,
    ReviewSerializer
)
from users.permissions import IsSuperUserIsAdminIsModeratorIsAuthor


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsSuperUserIsAdminIsModeratorIsAuthor,
    )

    def get_title_obj(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        title = self.get_title_obj()
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title_obj())


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class CategoryViewSet(ModelMixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUserIsAdminIsModeratorIsAuthor,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ModelMixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsSuperUserIsAdminIsModeratorIsAuthor,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSuperUserIsAdminIsModeratorIsAuthor,)
    http_method_names = ['get', 'post', 'patch', 'delete']

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
