# Generated by Django 4.0.6 on 2025-01-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0038_remove_expenseprofile_profile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseprofile',
            name='invoice',
            field=models.FileField(blank=True, help_text='Attach invoice PDF', null=True, upload_to='invoices/'),
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='invoice',
            field=models.FileField(blank=True, help_text='Invoice PDF from Expense Profile', null=True, upload_to='invoices/'),
        ),
    ]