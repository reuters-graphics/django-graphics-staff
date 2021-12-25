from django.urls import include, path
from rest_framework import routers

from .viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("api/", include(router.urls)),
]
