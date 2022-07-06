# Generated by Django 3.1.2 on 2021-03-26 09:37
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignKeyRelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'single_signal',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.mysinglesignalmodel'),
                ),
            ],
        ),
        migrations.CreateModel(
            name='CommonInfoBasedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created_at',
                    models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Erstellt am'),
                ),
                (
                    'lastmodified_at',
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, verbose_name='Zuletzt geändert am'
                    ),
                ),
                ('value', models.PositiveIntegerField(default=0)),
                (
                    'created_by',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='testapp_commoninfobasedmodel_created',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Erstellt von',
                    ),
                ),
                (
                    'lastmodified_by',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='testapp_commoninfobasedmodel_lastmodified',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Zuletzt geändert von',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
