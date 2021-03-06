# Generated by Django 4.0 on 2021-12-25 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Gmail')),
                ('google_display_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Display name')),
                ('twitter_handle', models.CharField(blank=True, max_length=250, null=True, verbose_name='Handle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
