from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор модели Category."""
    class Meta:
        model = Category
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор модели Genre."""
    class Meta:
        model = Genre
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериализатор модели Title."""
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Title
        fields = ('id', 'name', 'description', 'year', 'category', 'genre')
