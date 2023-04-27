from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_confirmation_code, get_token
from .views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                    ReviewViewSet, CommentViewSet)


router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/auth/signup/', get_confirmation_code, name='signup'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/', include('django.contrib.auth.urls')),
    path('v1/', include(router_v1.urls)),
