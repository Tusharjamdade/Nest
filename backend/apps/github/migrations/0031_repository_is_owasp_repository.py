# Generated by Django 5.1 on 2024-08-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("github", "0030_alter_release_sequence_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="repository",
            name="is_owasp_repository",
            field=models.BooleanField(default=False, verbose_name="Is OWASP repository"),
        ),
    ]