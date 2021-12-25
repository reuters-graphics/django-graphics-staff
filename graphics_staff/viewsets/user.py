from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from graphics_staff.conf import settings
from graphics_staff.serializers import UserSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (settings.API_AUTHENTICATION_CLASS,)
    permission_classes = (settings.API_PERMISSION_CLASS,)
    pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    queryset = User.objects.all()
    filterset_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
