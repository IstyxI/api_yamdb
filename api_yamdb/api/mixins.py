from rest_framework import filters
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin, ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from api.permissions import AnonimReadOnly, IsSuperUserOrIsAdminOnly


class ModelMixinSet(CreateModelMixin, ListModelMixin,
                    DestroyModelMixin, GenericViewSet):
    """Миксин для views.

    Миксин реализующий создание, вывод всех объектов, а также удаление объекта.
    """

    permission_classes = (AnonimReadOnly | IsSuperUserOrIsAdminOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
