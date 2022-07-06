# Generated by Django 3.1 on 2021-04-19 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0002_auto_210407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithFkToSelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'parent',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='children',
                        to='testapp.modelwithfktoself',
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name='foreignkeyrelatedmodel',
            name='single_signal',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='foreign_key_related_models',
                to='testapp.mysinglesignalmodel',
            ),
        ),
        migrations.AlterField(
            model_name='modelwithfktoself',
            name='parent',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='children',
                to='testapp.modelwithfktoself',
            ),
        ),
        migrations.CreateModel(
            name='ModelWithOneToOneToSelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'peer',
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='related_peer',
                        to='testapp.modelwithonetoonetoself',
                    ),
                ),
            ],
        ),
    ]
