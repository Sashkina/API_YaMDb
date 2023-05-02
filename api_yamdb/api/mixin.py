from rest_framework import status
from rest_framework.response import Response


class CRDViewSet(object):
    """mixin категории и жанры viewsets."""
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
