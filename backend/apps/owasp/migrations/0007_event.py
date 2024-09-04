# Generated by Django 5.1 on 2024-08-22 20:35

import django.db.models.deletion
from django.db import migrations, models

import apps.owasp.models.common


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0022_alter_organization_login_alter_user_login"),
        ("owasp", "0006_chapter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("nest_created_at", models.DateTimeField(auto_now_add=True)),
                ("nest_updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("key", models.CharField(max_length=100, unique=True, verbose_name="Key")),
                (
                    "description",
                    models.CharField(default="", max_length=500, verbose_name="Description"),
                ),
                ("level", models.CharField(default="", max_length=5, verbose_name="Level")),
                ("url", models.URLField(default="", verbose_name="URL")),
                ("tags", models.JSONField(default=list, verbose_name="Tags")),
                (
                    "owasp_repository",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="github.repository",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Events",
                "db_table": "owasp_events",
            },
            bases=(apps.owasp.models.common.OwaspEntity, models.Model),
        ),
    ]