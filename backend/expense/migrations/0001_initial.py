# Generated by Django 4.0 on 2021-12-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('description', models.CharField(max_length=50, verbose_name='descrição')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='data de pagamento')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='valor')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
            ],
            options={
                'verbose_name': 'despesa',
                'verbose_name_plural': 'despesas',
                'ordering': ('-payment_date',),
            },
        ),
    ]