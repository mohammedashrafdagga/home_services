# Generated by Django 4.2.1 on 2023-06-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_image_alter_profile_phone_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="phone_number",
        ),
    ]