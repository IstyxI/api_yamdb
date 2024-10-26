from django.contrib import admin

from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ['name__istartswith']
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ['name__istartswith']
    list_filter = ('name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Title)
class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = [
        'name__istartswith',
        'description__istartswith',
        'category__istartswith'
    ]
    list_filter = ('name', 'year', 'category')
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'title', 'author', 'score', 'pub_date')
    search_fields = [
        'title__istartswith',
        'text__istartswith',
        'author__istartswith'
    ]
    list_filter = ('author', 'score', 'pub_date')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'review', 'author', 'pub_date')
    search_fields = ['author__istartswith', 'text__istartswith']
    list_filter = ('author', 'pub_date')
    empty_value_display = '-пусто-'
