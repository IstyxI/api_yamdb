from django.db import models


class UserRoles(models.TextChoices):

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
