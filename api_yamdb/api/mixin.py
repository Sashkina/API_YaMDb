from rest_framework import status, viewsets, mixins
from rest_framework.response import Response


class CRDViewSet(mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    pass

