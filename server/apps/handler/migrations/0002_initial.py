# Generated by Django 4.2.10 on 2024-02-17 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handler', '0001_initial'),
        ('manifest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporter',
            name='manifest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporters', to='manifest.manifest'),
        ),
    ]