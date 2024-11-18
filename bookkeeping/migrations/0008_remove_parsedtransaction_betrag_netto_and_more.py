# Generated by Django 4.0.6 on 2024-11-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0007_expenseprofile_ust'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='betrag_netto',
        ),
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='ust',
        ),
        migrations.AlterField(
            model_name='expenseprofile',
            name='ust',
            field=models.IntegerField(choices=[(0, '0%'), (7, '7%'), (19, '19%')], default=19),
        ),
    ]
