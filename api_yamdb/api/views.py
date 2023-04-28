import django_filters
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly, IsAdminOrAuthorOrReadOnly

from reviews.models import Category, Genre, Title, Review
from .serializers import (CategorySerializer,GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer,
                          ReviewSerializer, CommentSerializer)


class TitleFilter(django_filters.FilterSet):
    """ Класс для создания фильтров. """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre__title', 'category__title')


class TitleViewSet(viewsets.ModelViewSet):
    """ Эндпоинт для работы с моделью Title. """
    permission_classes = (IsAdminOrReadOnly,)
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
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    """ Эндпоинт для работы с моделью Genre. """
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrAuthorOrReadOnly,)
    serializer_class = ReviewSerializer
    permission_classes = []

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, id=self.kwargs.get("title_id"))
        )


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrAuthorOrReadOnly,)
    serializer_class = CommentSerializer
    permission_classes = []

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        new_queryset = review.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(Review, id=self.kwargs.get("review_id"))
        )
