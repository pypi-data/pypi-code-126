# Generated by Django 2.1.2 on 2018-11-08 01:53

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_offstudy", "0002_auto_20180921_0434")]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectoffstudy",
            name="history_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        )
    ]
