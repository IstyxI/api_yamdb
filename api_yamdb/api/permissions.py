from rest_framework import permissions


class AnonimReadOnly(permissions.BasePermission):
    """Разрешает анонимному пользователю безопасные запросы."""

    def has_permission(self, request, view):
        """Проверяет является ли запрос 'безопасным'."""
        return request.method in permissions.SAFE_METHODS


class IsSuperUserOrIsAdminOnly(permissions.BasePermission):
    """Права на запросы.

    Права на запросы только для суперпользователя Джанго,
    админа Джанго или аутентифицированному пользователю с ролью admin.
    """

    def has_permission(self, request, view):
        """Проверяет есть ли у пользователя права на действие."""
        return (
            request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin)
        )


class IsSuperUserIsAdminIsModeratorIsAuthor(permissions.BasePermission):
    """Право анониму осуществлять только безопасные запросы.

    Доступ к запросам PATCH и DELETE предоставляется только
    суперпользователю Джанго, админу Джанго, аутентифицированным пользователям
    с ролью admin или moderator, а также автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        """Проверяет есть ли права на запрос."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin
                 or request.user.is_moderator
                 or request.user == obj.author)
        )
