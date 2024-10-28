from django.contrib import admin
from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка раздела категорий."""

    list_display = ('pk', 'name', 'slug')
    empty_value_display = 'none'
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Настройки раздела жанров."""

    list_display = ('pk', 'name', 'slug')
    empty_value_display = 'none'
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Title)
class GenreTitleAdmin(admin.ModelAdmin):
    """Настройка раздела жанров и произведений."""

    list_display = ('pk', 'name', 'year', 'description', 'category')
    empty_value_display = 'none'
    list_filter = ('name',)
    search_fields = ('name', 'year', 'category')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка раздела отзывов."""

    list_display = ('pk', 'text', 'title', 'author', 'score', 'pub_date')
    empty_value_display = 'none'
    list_filter = ('author', 'score', 'pub_date')
    search_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка раздела комментариев."""

    list_display = ('pk', 'text', 'review', 'author', 'pub_date')
    empty_value_display = 'значение отсутствует'
    list_filter = ('author', 'pub_date')
    search_fields = ('author',)


admin.site.site_title = 'Администрирование YamDb'
admin.site.site_header = 'Администрирование YamDb'
