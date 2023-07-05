# Generated by Django 4.2.1 on 2023-07-04 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0006_changeemail"),
        ("services", "0011_category_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomServices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("descriptions", models.TextField()),
                ("request_date", models.DateField()),
                ("request_time", models.TimeField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.category",
                    ),
                ),
                (
                    "location",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.location"
                    ),
                ),
                (
                    "request_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="custom_services",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]