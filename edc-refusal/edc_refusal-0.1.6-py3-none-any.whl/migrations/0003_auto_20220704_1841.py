# Generated by Django 3.2.13 on 2022-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_refusal", "0002_historicalsubjectrefusal"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalsubjectrefusal",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Subject Refusal",
                "verbose_name_plural": "historical Subject Refusals",
            },
        ),
        migrations.AlterField(
            model_name="historicalsubjectrefusal",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
