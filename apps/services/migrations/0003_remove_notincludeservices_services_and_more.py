# Generated by Django 4.2.1 on 2023-07-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_rename_created_by_services_user_services_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notincludeservices",
            name="services",
        ),
        migrations.DeleteModel(
            name="IncludeServices",
        ),
        migrations.DeleteModel(
            name="NotIncludeServices",
        ),
    ]
