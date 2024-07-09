# Generated by Django 5.0.2 on 2024-02-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                ("slug", models.CharField(max_length=255, verbose_name="Slug")),
                ("flag", models.CharField(max_length=255, verbose_name="Bandeira")),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]