# Generated by Django 4.1.1 on 2022-09-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("hashtags", models.CharField(max_length=200)),
                ("category", models.CharField(max_length=200)),
                ("associates", models.CharField(max_length=200)),
            ],
        ),
    ]
