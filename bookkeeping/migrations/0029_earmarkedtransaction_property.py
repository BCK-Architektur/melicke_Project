# Generated by Django 4.0.6 on 2024-12-19 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0028_alter_lease_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='earmarkedtransaction',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.property'),
        ),
    ]