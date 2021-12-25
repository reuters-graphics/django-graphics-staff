from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .group import GroupSerializer
from .profile import ProfileSerializer
from .user_social_auth import UserSocialAuthSerializer


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    social_ids = UserSocialAuthSerializer(source="social_auth", many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "profile",
            "social_ids",
            "groups",
        )
        extra_kwargs = {"url": {"lookup_field": "email"}}
