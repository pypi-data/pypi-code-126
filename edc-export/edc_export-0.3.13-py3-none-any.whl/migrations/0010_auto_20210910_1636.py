# Generated by Django 3.2.6 on 2021-09-10 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edc_export", "0009_auto_20210510_2036"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exportdata",
            options={
                "permissions": [("display_export_admin_action", "Display export action")]
            },
        ),
        migrations.AlterModelOptions(
            name="importdata",
            options={
                "permissions": [("display_import_admin_action", "Display import action")]
            },
        ),
    ]
