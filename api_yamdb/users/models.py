from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.enums import UserRoles


class User(AbstractUser):
    
    username = models.CharField(
        max_length=150,
        verbose_name='Никнейм',
        unique=True,
        db_index=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Никнейм содержит недопустимый символ.'
        )]
    )

    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True
    )

    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        blank=True
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=True
    )

    role = models.CharField(
        max_length=32,
        verbose_name='Роль',
        choices=UserRoles.choices(),
        default=UserRoles.user.name
    )

    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )

    confirmation_code = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Код подтверждения',
        help_text='Введите код подтверждения из письма',
    )

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('username', 'id')
        verbose_name = 'User'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == UserRoles.admin.name

    @property
    def is_moderator(self):
        return self.role == UserRoles.moderator.name

    @property
    def is_user(self):
        return self.role == UserRoles.user.name

    def __str__(self):
        return self.username
