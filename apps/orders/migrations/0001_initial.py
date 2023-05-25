# Generated by Django 4.2.1 on 2023-05-25 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("services", "0009_notincludeservices_includeservices"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("قيد المراجعة", "قيد المراجعة"),
                            ("قيد التنفيذ", "قيد المراجعة"),
                            ("مكتمل", "مكتمل"),
                        ],
                        default="قيد المراجعة",
                        max_length=12,
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("total_price", models.PositiveIntegerField(blank=True, null=True)),
                ("date_order", models.DateField()),
                ("time_order", models.TimeField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "create_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to="services.services",
                    ),
                ),
            ],
        ),
    ]
