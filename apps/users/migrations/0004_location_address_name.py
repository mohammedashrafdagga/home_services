# Generated by Django 4.2.1 on 2023-07-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customservices_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="address_name",
            field=models.CharField(default="address_one", max_length=250),
            preserve_default=False,
        ),
    ]