# Generated by Django 4.0.6 on 2024-11-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0004_alter_earmarkedtransaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parsedtransaction',
            old_name='expense_profile',
            new_name='gggkto',
        ),
        migrations.RemoveField(
            model_name='expenseprofile',
            name='iban',
        ),
        migrations.RemoveField(
            model_name='expenseprofile',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='description',
        ),
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='is_income',
        ),
        migrations.RemoveField(
            model_name='parsedtransaction',
            name='tenant',
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='name',
            field=models.CharField(default='default', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='transactions',
            field=models.ManyToManyField(blank=True, related_name='expense_profiles', to='bookkeeping.parsedtransaction'),
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='ust',
            field=models.IntegerField(choices=[(0, '0%'), (19, '19%')], default=19),
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='ust_sch',
            field=models.CharField(choices=[('Nicht', 'Nicht'), ('Voll', 'Voll'), ('Teilw', 'Teilw')], default='Voll', max_length=10),
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='betrag_brutto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='betrag_netto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parsedtransaction',
            name='ust',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
