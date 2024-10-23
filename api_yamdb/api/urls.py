from django.urls import include, path

from rest_framework import routers

from api.views import (
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet,
    CommentViewSet,
    ReviewViewSet
)

router = routers.DefaultRouter()
router.register('titles', TitleViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
