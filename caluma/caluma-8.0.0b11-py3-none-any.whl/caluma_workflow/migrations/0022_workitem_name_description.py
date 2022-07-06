# Generated by Django 2.2.10 on 2020-03-19 09:15

import localized_fields.fields.field
from django.db import migrations


def set_name_and_description(apps, schema_editor):
    WorkItem = apps.get_model("caluma_workflow", "WorkItem")
    HistoricalWorkItem = apps.get_model("caluma_workflow", "HistoricalWorkItem")
    db_alias = schema_editor.connection.alias

    for work_item in WorkItem.objects.using(db_alias).iterator():
        work_item.name = work_item.task.name
        work_item.description = work_item.task.description
        work_item.save()
        for historical_work_item in HistoricalWorkItem.objects.using(db_alias).filter(
            id=work_item.pk
        ):
            historical_work_item.name = work_item.name
            historical_work_item.description = work_item.description
            historical_work_item.save()


class Migration(migrations.Migration):

    dependencies = [("caluma_workflow", "0021_work_item_controlling_groups")]

    operations = [
        migrations.AddField(
            model_name="historicalworkitem",
            name="description",
            field=localized_fields.fields.field.LocalizedField(
                blank=True,
                help_text="Will be set from Task, if not provided.",
                null=True,
                required=[],
            ),
        ),
        migrations.AddField(
            model_name="historicalworkitem",
            name="name",
            field=localized_fields.fields.field.LocalizedField(
                default={"de": "temp_placeholder"},
                help_text="Will be set from Task, if not provided.",
                required=[],
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="workitem",
            name="description",
            field=localized_fields.fields.field.LocalizedField(
                blank=True,
                help_text="Will be set from Task, if not provided.",
                null=True,
                required=[],
            ),
        ),
        migrations.AddField(
            model_name="workitem",
            name="name",
            field=localized_fields.fields.field.LocalizedField(
                default={"de": "temp_placeholder"},
                help_text="Will be set from Task, if not provided.",
                required=[],
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_name_and_description, migrations.RunPython.noop),
    ]
