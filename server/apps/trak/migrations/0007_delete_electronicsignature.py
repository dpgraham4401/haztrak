# Generated by Django 4.0.4 on 2022-06-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0006_alter_address_country_alter_address_state'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ElectronicSignature',
        ),
    ]