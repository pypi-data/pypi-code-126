# Generated by Django 3.2.6 on 2021-09-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_unblinding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalunblindingrequest',
            name='requestor',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Choose a name from the list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_unblinding.unblindingrequestoruser', verbose_name='Unblinding requested by'),
        ),
        migrations.AlterField(
            model_name='historicalunblindingreview',
            name='reviewer',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Choose a name from the list', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_unblinding.unblindingrevieweruser', verbose_name='Unblinding request reviewed by'),
        ),
        migrations.AlterField(
            model_name='unblindingrequest',
            name='requestor',
            field=models.ForeignKey(help_text='Choose a name from the list', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_unblinding.unblindingrequestoruser', verbose_name='Unblinding requested by'),
        ),
        migrations.AlterField(
            model_name='unblindingreview',
            name='reviewer',
            field=models.ForeignKey(help_text='Choose a name from the list', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='edc_unblinding.unblindingrevieweruser', verbose_name='Unblinding request reviewed by'),
        ),
    ]
