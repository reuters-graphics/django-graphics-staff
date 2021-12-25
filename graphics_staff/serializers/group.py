from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from .permission import PermissionSerializer


class GroupSerializer(ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ("name", "permissions")
