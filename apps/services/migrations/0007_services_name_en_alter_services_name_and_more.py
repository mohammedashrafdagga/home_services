# Generated by Django 4.2.1 on 2023-05-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0006_alter_services_price_from_alter_services_price_to"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="name_en",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="services",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="services",
            name="slug",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
