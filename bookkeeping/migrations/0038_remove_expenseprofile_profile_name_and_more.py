# Generated by Django 4.0.6 on 2025-01-07 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0037_alter_expenseprofile_booking_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenseprofile',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='incomeprofile',
            name='profile_name',
        ),
    ]
