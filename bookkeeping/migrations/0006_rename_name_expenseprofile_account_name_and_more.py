# Generated by Django 4.0.6 on 2024-11-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0005_rename_expense_profile_parsedtransaction_gggkto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenseprofile',
            old_name='name',
            new_name='account_name',
        ),
        migrations.RemoveField(
            model_name='expenseprofile',
            name='ust',
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='profile_name',
            field=models.CharField(default='Default', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]