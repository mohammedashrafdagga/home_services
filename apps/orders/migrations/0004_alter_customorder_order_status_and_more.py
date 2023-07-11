# Generated by Django 4.2.1 on 2023-07-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_rename_created_by_customorder_create_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customorder",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("قيد المراجعة", "قيد المراجعة"),
                    ("قيد التنفيذ", "قيد المراجعة"),
                    ("مكتمل", "مكتمل"),
                    ("مرفوض", "مرفوض"),
                ],
                default="قيد المراجعة",
                max_length=12,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("قيد المراجعة", "قيد المراجعة"),
                    ("قيد التنفيذ", "قيد المراجعة"),
                    ("مكتمل", "مكتمل"),
                    ("مرفوض", "مرفوض"),
                ],
                default="قيد المراجعة",
                max_length=12,
            ),
        ),
    ]
