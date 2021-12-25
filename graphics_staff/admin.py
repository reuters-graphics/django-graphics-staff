from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

from graphics_staff.models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "user profile"
    fieldsets = (
        (None, {"fields": ("user",)}),
        ("Google", {"fields": ("google_email", "google_display_name")}),
        ("Twitter", {"fields": ("twitter_handle",)}),
    )


class SocialInlineAdmin(admin.StackedInline):
    model = UserSocialAuth
    can_delete = False
    extra = 0
    verbose_name_plural = "social auth"
    fieldsets = ((None, {"fields": ("user", "provider", "uid", "extra_data")}),)


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
        SocialInlineAdmin,
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
