# Generated by Django 4.2.1 on 2023-05-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_alter_category_last_update"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]