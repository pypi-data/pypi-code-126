# Generated by Django 2.2.22 on 2021-11-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caluma_form", "0040_add_modified_by_user_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalquestion",
            name="type",
            field=models.CharField(
                choices=[
                    ("multiple_choice", "multiple_choice"),
                    ("integer", "integer"),
                    ("float", "float"),
                    ("date", "date"),
                    ("choice", "choice"),
                    ("textarea", "textarea"),
                    ("text", "text"),
                    ("table", "table"),
                    ("form", "form"),
                    ("file", "file"),
                    ("dynamic_choice", "dynamic_choice"),
                    ("dynamic_multiple_choice", "dynamic_multiple_choice"),
                    ("static", "static"),
                    ("calculated_float", "calculated_float"),
                    ("action_button", "action_button"),
                ],
                max_length=23,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("multiple_choice", "multiple_choice"),
                    ("integer", "integer"),
                    ("float", "float"),
                    ("date", "date"),
                    ("choice", "choice"),
                    ("textarea", "textarea"),
                    ("text", "text"),
                    ("table", "table"),
                    ("form", "form"),
                    ("file", "file"),
                    ("dynamic_choice", "dynamic_choice"),
                    ("dynamic_multiple_choice", "dynamic_multiple_choice"),
                    ("static", "static"),
                    ("calculated_float", "calculated_float"),
                    ("action_button", "action_button"),
                ],
                max_length=23,
            ),
        ),
    ]
