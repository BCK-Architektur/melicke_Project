# Generated by Django 4.0.6 on 2024-11-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0009_alter_parsedtransaction_gggkto'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseprofile',
            name='BN_no',
            field=models.IntegerField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
