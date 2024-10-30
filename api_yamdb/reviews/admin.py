from django.contrib import admin

from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка раздела категорий."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ['name__istartswith', 'name']
    list_filter = ('name', 'slug')
    empty_value_display = 'none'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Настройка раздела жанров."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ['name__istartswith', 'name']
    list_filter = ('name', 'slug')
    empty_value_display = 'none'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Title)
class GenreTitleAdmin(admin.ModelAdmin):
    """Настройка раздела жанров и произведений."""

    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = [
        'name__istartswith',
        'description__istartswith',
        'category__istartswith',
        'name', 'year', 'category'
    ]
    list_filter = ('name', 'year', 'category')
    empty_value_display = 'none'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка раздела отзывов."""

    list_display = ('pk', 'text', 'title', 'author', 'score', 'pub_date')
    search_fields = [
        'title__istartswith',
        'text__istartswith',
        'author__istartswith'
    ]
    list_filter = ('author', 'score', 'pub_date')
    empty_value_display = 'none'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка раздела комментариев."""

    list_display = ('pk', 'text', 'review', 'author', 'pub_date')
    search_fields = ['author__istartswith', 'author', 'text__istartswith']
    list_filter = ('author', 'pub_date')
    empty_value_display = 'none'


admin.site.site_title = 'Администрирование YamDb'
admin.site.site_header = 'Администрирование YamDb'
