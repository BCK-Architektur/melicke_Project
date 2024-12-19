# Generated by Django 4.0.6 on 2024-12-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0029_earmarkedtransaction_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsedtransaction',
            name='is_income',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='tenant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
