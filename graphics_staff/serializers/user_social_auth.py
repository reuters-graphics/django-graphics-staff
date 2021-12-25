from rest_framework.serializers import ModelSerializer
from social_django.models import UserSocialAuth


class UserSocialAuthSerializer(ModelSerializer):
    class Meta:
        model = UserSocialAuth
        fields = (
            "uid",
            "provider",
            "extra_data",
        )
