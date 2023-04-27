from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from reviews.models import Category, Genre, Title, Review

from .serializers import (CategorySerializer,GenreSerializer,
                          TitleSerializer, ReviewSerializer,
                          CommentSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
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

