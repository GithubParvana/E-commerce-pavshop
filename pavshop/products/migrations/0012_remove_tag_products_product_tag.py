# Generated by Django 4.1.7 on 2023-07-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='products.tag'),
        ),
    ]
