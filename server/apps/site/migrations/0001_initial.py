# Generated by Django 4.2.10 on 2024-02-16 21:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('org', '0001_initial'),
        ('rcrasite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HaztrakSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'site aliases must be longer than 2 characters')], verbose_name='site alias')),
                ('last_rcrainfo_manifest_sync', models.DateTimeField(blank=True, null=True, verbose_name='last RCRAInfo manifest sync date')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.haztrakorg')),
                ('rcra_site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rcrasite.rcrasite', verbose_name='rcra_site')),
            ],
            options={
                'verbose_name': 'Haztrak Site',
                'verbose_name_plural': 'Haztrak Sites',
                'ordering': ['rcra_site__epa_id'],
            },
        ),
        migrations.CreateModel(
            name='SitePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emanifest', models.CharField(choices=[('viewer', 'view'), ('editor', 'edit'), ('signer', 'sign')], default='view', max_length=6)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_permissions', to='core.haztrakprofile')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site.haztraksite')),
            ],
            options={
                'verbose_name': 'Site Permission',
                'verbose_name_plural': 'Site Permissions',
                'ordering': ['profile'],
            },
        ),
    ]
