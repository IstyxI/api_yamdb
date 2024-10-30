from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


class UserAdmin(BaseUserAdmin):
    """Модель админа."""

    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role'
    )
    empty_value_display = 'none'
    list_editable = ('role',)
    list_filter = ('username', 'id')
    search_fields = ('username', 'role')


admin.site.register(User, UserAdmin)
