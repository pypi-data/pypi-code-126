# Generated by Django 2.0.1 on 2018-01-16 13:28

import django.contrib.sites.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("edc_locator", "0005_auto_20180116_1411")]

    operations = [
        migrations.AlterModelManagers(
            name="subjectlocator",
            managers=[("on_site", django.contrib.sites.managers.CurrentSiteManager())],
        )
    ]
