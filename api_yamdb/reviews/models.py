from django.db import models


class Category(models.Model):
    """Модель, описывающая категории произведений."""
    name = models.CharField(max_length=255, verbose_name=('Категория'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=('URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Категории')
        ordering = ['id']


class Genre(models.Model):
    """Модель, описывающая жанры произведений."""
    name = models.CharField(max_length=100, verbose_name=('Название'))
    slug = models.SlugField(unique=True, verbose_name=('URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Title(models.Model):
    """Модель, описывающая произведения."""
    name = models.CharField(max_length=100, verbose_name=('Название'))
    year = models.IntegerField(verbose_name=('Год выпуска'))
    description = models.TextField(null=True, blank=True, verbose_name=('Описание'))
    genre = models.ManyToManyField(
        Genre, related_name='title', verbose_name=('URL жанра'))
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='title',
        verbose_name=('URL категории')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name', 'description']
