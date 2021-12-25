![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-graphics_staff

## Quickstart

1. Install the app from GitHub:

   ```bash
   pipenv install -e git+https://github.com/reuters-graphics/django-graphics-staff.git#egg=django-graphics_staff
   ```

2. Add "graphics_staff" to your INSTALLED_APPS and other settings like this:

   ```python
   INSTALLED_APPS = [
      # ...
      "graphics_staff",
      "rest_framework",
      "django_filters",
      "social_django",
   ]

   SOCIAL_AUTH_JSONFIELD_ENABLED = False if DEBUG else True

   AUTHENTICATION_BACKENDS = (
      # Other social auth backends
      "django.contrib.auth.backends.ModelBackend",
   )
   ```

3. Include the graphics_staff URLconf in your project's `urls.py` like this:

   ```python
   from django.urls import include, path

   urlpatterns = [
      # ...
      path("graphics-staff/", include("graphics_staff.urls")),
   ]
   ```

4. Run `python manage.py migrate` to create the graphics_staff models.

## Developing

Read more about developing this app in the [Developing](./DEVELOPING.md) docs.
