from django.contrib.auth.models import User
from django.db import models
from graphics_staff.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Google
    google_email = models.EmailField(blank=True, null=True, verbose_name="Gmail")
    google_display_name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Display name"
    )

    # twitter
    twitter_handle = models.CharField(max_length=250, blank=True, null=True, verbose_name="Handle")

    def __str__(self):
        return self.user.email
