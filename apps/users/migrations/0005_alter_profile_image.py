# Generated by Django 4.2.1 on 2023-07-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_location_address_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_images/placeholder.jpg",
                help_text="صورة شخصية",
                upload_to="profile_images",
            ),
        ),
    ]
