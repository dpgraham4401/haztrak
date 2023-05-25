# Generated by Django 4.1.7 on 2023-05-11 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("trak", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CorrectionInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("version_number", models.IntegerField(blank=True, null=True)),
                ("active", models.BooleanField(blank=True, null=True)),
                ("ppc_active", models.BooleanField(blank=True, null=True)),
                ("epa_site_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "initiator_role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("IN", "Industry"),
                            ("PP", "Ppc"),
                            ("EP", "Epa"),
                            ("ST", "State"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "update_role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("IN", "Industry"),
                            ("PP", "Ppc"),
                            ("EP", "Epa"),
                            ("ST", "State"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "electronic_signature_info",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trak.esignature",
                    ),
                ),
            ],
            options={
                "verbose_name": "Correction Info",
                "verbose_name_plural": "Correction Info",
            },
        ),
    ]