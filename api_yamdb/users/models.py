from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    MODERATOR = 'moderator'

    USER_ROLES = [
        (ADMIN, 'Admin role'),
        (USER, 'User role'),
        (MODERATOR, 'Moderator role')
    ]

    email = models.EmailField(
        max_length=128,
        unique=True,
        verbose_name='email'
    )
    role = models.CharField(
        max_length=16,
        choices=USER_ROLES,
        default='user',
        verbose_name='Роль'
    )
    token = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )
    bio = models.TextField(
        max_length=256,
        blank=True,
        verbose_name='Биография'
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'user'
        verbose_name_plural = 'Пользователи'

    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    def is_moderator(self):
        return self.role == self.MODERATOR

    def __str__(self):
        return self.username
