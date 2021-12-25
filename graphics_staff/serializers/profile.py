from graphics_staff.models import Profile
from rest_framework.serializers import ModelSerializer


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "google_email",
            "google_display_name",
            "twitter_handle",
        )
