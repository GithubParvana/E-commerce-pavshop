# Generated by Django 4.1.7 on 2023-06-28 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_discount_value_currency_alter_discount_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='value_currency',
        ),
        migrations.RemoveField(
            model_name='product',
            name='money_currency',
        ),
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='money',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
