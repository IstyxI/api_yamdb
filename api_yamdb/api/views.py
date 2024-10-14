from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Title, Category, Genre

from .serializers import TitleSerializer, CategorySerializer, GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('slug', 'genre', 'name', 'year')


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)
