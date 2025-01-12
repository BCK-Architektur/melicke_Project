# Generated by Django 4.0.6 on 2024-12-04 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookkeeping', '0016_lease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenseprofile',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='expenseprofile',
            name='transactions',
        ),
        migrations.RemoveField(
            model_name='expenseprofile',
            name='ust_sch',
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='frequency',
            field=models.CharField(blank=True, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='lease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_profiles', to='bookkeeping.lease'),
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expenseprofile',
            name='transaction_type',
            field=models.CharField(choices=[('repair', 'Repair'), ('maintenance', 'Maintenance'), ('other', 'Other')], default='other', max_length=50),
        ),
        migrations.AlterField(
            model_name='expenseprofile',
            name='account_name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='IncomeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('rent', 'Rent'), ('deposit', 'Deposit')], default='rent', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('recurring', models.BooleanField(default=False)),
                ('frequency', models.CharField(blank=True, choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10, null=True)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_profiles', to='bookkeeping.lease')),
            ],
        ),
    ]
