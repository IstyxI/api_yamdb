from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Конфиг."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователи'
