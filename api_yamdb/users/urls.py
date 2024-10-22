from django.urls import include, path
from rest_framework import routers

from users.views import (
    UserCreateViewSet,
    UserReceiveTokenViewSet,
    UserViewSet
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
auth_urls = [
    path(
        'signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]

urlpatterns = [
    path('v1/auth/', include(auth_urls)),
    path('v1/', include(router.urls))
]
