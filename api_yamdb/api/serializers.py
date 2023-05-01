from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


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
    """Сериализатор модели чтение Title."""
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Title
        fields = ('id',
                  'name',
                  'description',
                  'year',
                  'category',
                  'genre',
                  'rating')


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериализатор модели создания Title."""
    genre = serializers.SlugRelatedField(
        many=True, slug_field='slug', queryset=Genre.objects.all())
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all())
    rating = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False)
    year = serializers.IntegerField(required=True)

    class Meta:
        model = Title
        fields = ('id',
                  'name',
                  'description',
                  'year',
                  'category',
                  'genre',
                  'rating')


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор модели Review."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id',
                  'author',
                  'text',
                  'score',
                  'title',
                  'pub_date')
        model = Review
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Comment."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id',
                  'author',
                  'review',
                  'text',
                  'pub_date')
        model = Comment
        read_only_fields = ('review',)
