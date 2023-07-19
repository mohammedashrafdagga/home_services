# Generated by Django 4.2.1 on 2023-07-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_remove_notincludeservices_services_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="services",
            name="slug",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
