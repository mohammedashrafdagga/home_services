# Generated by Django 4.2.1 on 2023-05-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_services"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="price_from",
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name="services",
            name="price_to",
            field=models.PositiveIntegerField(default=50),
        ),
    ]
