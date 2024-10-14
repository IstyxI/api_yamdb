from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Genre(models.Model):
    name = models.CharField('Название группы', max_length=256, blank=False)
    slug = models.SlugField('Слаг', unique=True, max_length=50, blank=False)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название группы', max_length=256, blank=False)
    slug = models.SlugField('Слаг', unique=True, max_length=50, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField('Название', max_length=256, blank=False)
    year = models.IntegerField('Год выпуска', blank=False)
    description = models.TextField('Описание', blank=True)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Жанр',
        blank=False,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='titles',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return f'{self.name[:20]}...'


class Review(models.Model):
    text = models.TextField('Название', max_length=256, blank=False)


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'коментарии'
