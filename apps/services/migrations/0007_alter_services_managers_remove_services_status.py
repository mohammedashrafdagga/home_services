# Generated by Django 4.2.1 on 2023-07-19 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0006_alter_services_managers_alter_services_image_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="services",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="services",
            name="status",
        ),
    ]
