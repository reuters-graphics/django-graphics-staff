"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""

from django.conf import settings as project_settings
from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication, exceptions

from graphics_staff.utils.importers import import_class


class Settings:
    pass


Settings.SECRET_TOKEN = getattr(project_settings, "GRAPHICS_STAFF_SECRET_TOKEN", "SECRET")

Settings.AUTH_DECORATOR = getattr(
    project_settings,
    "GRAPHICS_STAFF_AUTH_DECORATOR",
    "django.contrib.admin.views.decorators.staff_member_required",
)


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Don't enforce if DEBUG
        if project_settings.DEBUG:
            return (AnonymousUser, None)
        try:
            # Per DRF token auth, token is prefixed by string
            # literal "Token" plus whitespace, e.g., "Token <AUTHTOKEN>"
            token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        except Exception:
            raise exceptions.AuthenticationFailed("No token or incorrect token format")

        if token == Settings.SECRET_TOKEN:
            return (AnonymousUser, None)
        raise exceptions.AuthenticationFailed("Unauthorized")


if hasattr(project_settings, "STAFF_API_AUTHENTICATION_CLASS"):
    Settings.API_AUTHENTICATION_CLASS = import_class(
        getattr(
            project_settings,
            "STAFF_API_AUTHENTICATION_CLASS",
        )
    )
else:
    Settings.API_AUTHENTICATION_CLASS = TokenAuthentication

Settings.API_PERMISSION_CLASS = import_class(
    getattr(
        project_settings,
        "STAFF_API_PERMISSION_CLASS",
        "rest_framework.permissions.IsAuthenticated",
    )
)


settings = Settings
