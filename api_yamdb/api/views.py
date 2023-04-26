import django_filters
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, GenreSerializer, TitleReadSerializer, TitleWriteSerializer
from reviews.models import Category, Genre, Title


class TitleFilter(django_filters.FilterSet):
    """ Класс для создания фильтров. """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre__title', 'category__title')


class TitleViewSet(viewsets.ModelViewSet):
    """ Эндпоинт для работы с моделью Title. """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_queryset(self):
        """ Фильтрация объектов по категории и жанру. """
        queryset = Title.objects.all()
        category = self.request.query_params.get('category')
        genre = self.request.query_params.get('genre')
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        if genre is not None:
            queryset = queryset.filter(genre__slug=genre)
        return queryset

    def get_serializer_class(self):
        """Определяет какой сериализатор будет использоваться
              для разных типов запроса."""
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ Эндпоинт для работы с моделью Category. """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    """ Эндпоинт для работы с моделью Genre. """
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
